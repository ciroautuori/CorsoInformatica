import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 2.4", page_icon="💻", layout="wide")

st.write("# Lezione 2.3: PEC: cos'è e come utilizzarla")
st.image("./src/img/banner.jpg", width=None)
# st.audio("./src/audio/Pec.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
         ## Obiettivi della lezione
         - Comprendere cos'è la PEC e la sua importanza
         - Imparare a configurare e utilizzare una PEC
         - Conoscere gli aspetti legali della PEC

         ## Contenuti

         ### 1. Introduzione alla PEC

         #### Cos'è la PEC
         - Definizione di Posta Elettronica Certificata
         - Differenze tra email normale e PEC
         - Valore legale della PEC
         - Quando è obbligatoria

         #### Caratteristiche principali
         - Certificazione dell'invio
         - Certificazione della consegna
         - Marca temporale
         - Integrità del messaggio

         ### 2. Attivazione e Configurazione

         #### Scelta del provider
         - Provider autorizzati
         - Costi e tipologie di abbonamento
         - Procedura di attivazione

         #### Configurazione
         - Accesso al servizio
         - Impostazioni di sicurezza
         - Configurazione client di posta
         - Gestione delle notifiche

         ### 3. Utilizzo della PEC

         #### Invio messaggi
         - Composizione messaggio PEC
         - Gestione allegati
         - Ricevute di accettazione
         - Ricevute di consegna

         #### Gestione
         - Organizzazione messaggi
         - Archiviazione
         - Conservazione delle ricevute
         - Backup dei messaggi

         ### 4. Aspetti Legali e Sicurezza

         #### Validità legale
         - Normativa di riferimento
         - Valore probatorio
         - Tempistiche di conservazione
         - Obblighi di legge

         #### Sicurezza
         - Autenticazione forte
         - Cifratura dei messaggi
         - Conservazione sicura
         - Gestione delle password

         ## Esercizi Pratici
         1. Configurazione PEC:
            - Accedi al servizio PEC
            - Configura le impostazioni base
            - Imposta la firma digitale

         2. Utilizzo base:
            - Invia un messaggio PEC
            - Verifica le ricevute
            - Salva e archivia le ricevute
            - Gestisci gli allegati

         3. Gestione avanzata:
            - Organizza i messaggi in cartelle
            - Imposta filtri
            - Crea backup dei messaggi importanti

         ## Verifica Apprendimento
         - Comprendi la differenza tra email e PEC?
         - Sai gestire l'invio e la ricezione di PEC?
         - Conosci il valore legale della PEC?
         - Sai gestire le ricevute PEC? 
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
