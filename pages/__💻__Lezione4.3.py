import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 4.3", page_icon="💻", layout="wide")

st.write("# Lezione 4.3: Calendario digitale e gestione appuntamenti")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/AgendaOnline.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Comprendere l'utilità dei calendari digitali
            - Imparare a utilizzare Google Calendar
            - Gestire appuntamenti e promemoria
            - Organizzare eventi e condividere il calendario

            ## Contenuti

            ### 1. Introduzione al Calendario Digitale

            #### Vantaggi del Calendario Digitale
            - Sincronizzazione su tutti i dispositivi
            - Condivisione con altri utenti
            - Notifiche e promemoria
            - Integrazione con email e altri servizi

            #### Principali Strumenti
            - Google Calendar
            - Outlook Calendar
            - Apple Calendar
            - Confronto e scelta del servizio

            ### 2. Google Calendar Base

            #### Configurazione Iniziale
            - Accesso con account Google
            - Impostazioni base del calendario
            - Personalizzazione vista
            - Configurazione notifiche

            #### Gestione Eventi
            - Creare un nuovo evento
            - Impostare data e ora
            - Aggiungere luogo
            - Inserire descrizione
            - Allegare documenti

            ### 3. Funzionalità Avanzate

            #### Organizzazione Eventi
            - Eventi ricorrenti
            - Calendario multipli
            - Codici colore
            - Tag e categorie
            - Priorità

            #### Collaborazione
            - Invitare partecipanti
            - Gestire le risposte
            - Condividere calendari
            - Permessi di accesso
            - Visualizzazione disponibilità

            ### 4. Produttività

            #### Integrazione
            - Sincronizzazione con smartphone
            - Collegamenti con email
            - Integrazione con Meet/Zoom
            - App di terze parti

            #### Ottimizzazione
            - Pianificazione efficiente
            - Gestione del tempo
            - Evitare sovrapposizioni
            - Backup degli eventi

            ## Esercizi Pratici

            1. Configurazione base:
            - Configura Google Calendar
            - Personalizza le impostazioni
            - Imposta le notifiche
            - Crea calendari multipli

            2. Gestione eventi:
            - Crea eventi singoli
            - Imposta eventi ricorrenti
            - Invita partecipanti
            - Gestisci le risposte

            3. Organizzazione avanzata:
            - Pianifica una settimana tipo
            - Usa i codici colore
            - Condividi calendari
            - Sincronizza dispositivi

            ## Verifica Apprendimento
            - Sai creare e gestire eventi?
            - Utilizzi efficacemente le notifiche?
            - Gestisci correttamente le condivisioni?
            - Mantieni organizzato il calendario?

            ## Suggerimenti Pratici
            - Controlla regolarmente il calendario
            - Imposta notifiche appropriate
            - Mantieni aggiornati gli eventi
            - Fai backup periodici
                        
        """)

st.markdown("---")
st.markdown("""📝 Nota: Questa lezione conclude il Modulo 2. Prima di procedere al Modulo 3, assicurati di aver acquisito tutte le competenze necessarie sulla comunicazione digitale. 
    """)

# Right column with chat interface
with right_col:
    st.markdown("### Assistente Virtuale")

    # Initialize chat history in session state if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Configure the model
    llm = ChatOpenAI(
        model="mistral-nemo-instruct-2407",
        openai_api_key="not-needed",
        openai_api_base="http://localhost:1234/v1",
        temperature=0.1,
        max_tokens=2048,
    )

    # Template for questions
    template = """
    Domanda: {question}
    Risposta pensata e dettagliata:"""

    # Create prompt
    prompt = PromptTemplate(
        input_variables=["question"],
        template=template
    )

    # Create chain
    chain = prompt | llm

    # Create container for chat history
    chat_container = st.container()

    # Display chat history
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Input for new question
    question = st.chat_input("Inserisci la tua domanda qui.")

    if question:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": question})

        # Display user message
        with st.chat_message("user"):
            st.markdown(question)

        # Get and display assistant response
        with st.chat_message("assistant"):
            response = chain.invoke({"question": question})
            clean_response = response.content if hasattr(
                response, 'content') else str(response)
            st.markdown(clean_response)

            # Add assistant response to chat history
            st.session_state.messages.append(
                {"role": "assistant", "content": clean_response})

    # Add a button to clear chat history
    if st.button("Cancella Cronologia Chat"):
        st.session_state.messages = []
        st.rerun()
