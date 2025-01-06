import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 5.2", page_icon="💻", layout="wide")

st.write("# Lezione 5.2: Riconoscere e evitare truffe online")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/TruffeOnline.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Imparare a riconoscere le truffe online più comuni
            - Sviluppare un approccio critico alla navigazione
            - Proteggere i propri dati personali e finanziari
            - Acquisire buone pratiche di sicurezza online

            ## Contenuti

            ### 1. Tipologie di Truffe Online

            #### Phishing
            - Cos'è il phishing
            - Email fraudolente
            - Siti web contraffatti
            - SMS truffa (smishing)
            - Chiamate sospette (vishing)

            #### Altre Truffe Comuni
            - Truffe dello shopping online
            - Falsi investimenti
            - Truffe romantiche
            - Finte vincite e lotterie
            - Crypto scam

            ### 2. Segnali d'Allarme

            #### Indicatori di Phishing
            - Mittenti sospetti
            - Errori grammaticali
            - Richieste urgenti
            - Link sospetti
            - Richieste di dati sensibili

            #### Siti Web Non Sicuri
            - Mancanza di HTTPS
            - URL sospetti
            - Design poco professionale
            - Prezzi troppo vantaggiosi
            - Metodi di pagamento non sicuri

            ### 3. Protezione e Prevenzione

            #### Misure di Sicurezza
            - Verifica delle fonti
            - Controllo URL
            - Aggiornamenti software
            - Antivirus attivo
            - Firewall configurato

            #### Comportamenti Sicuri
            - Non aprire allegati sospetti
            - Verificare i mittenti
            - Mai condividere dati sensibili
            - Usare password uniche
            - Monitorare conti bancari

            ### 4. Gestione Incidenti

            #### Cosa Fare Se
            - Hai cliccato su un link sospetto
            - Hai fornito dati personali
            - Hai subito un addebito non autorizzato
            - Hai ricevuto minacce online

            #### Segnalazione e Supporto
            - Contattare la Polizia Postale
            - Avvisare la banca
            - Bloccare carte compromesse
            - Cambiare password

            ## Esercizi Pratici

            1. Riconoscimento truffe:
            - Analizza email sospette
            - Identifica siti non sicuri
            - Valuta offerte commerciali
            - Verifica mittenti

            2. Simulazione scenari:
            - Gestisci tentativi di phishing
            - Valuta sicurezza siti web
            - Proteggi dati personali
            - Segnala incidenti

            3. Prevenzione attiva:
            - Configura filtri antispam
            - Imposta protezioni browser
            - Crea piano di emergenza
            - Organizza backup dati

            ## Verifica Apprendimento
            - Riconosci le truffe comuni?
            - Sai proteggere i tuoi dati?
            - Conosci le procedure di emergenza?
            - Applichi le misure preventive?

            ## Suggerimenti Pratici
            - Mantieni sempre alta l'attenzione
            - Verifica più volte prima di agire
            - Non farti prendere dalla fretta
            - Meglio essere cauti che pentirsi
            - Condividi le informazioni con prudenza            
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
        model="mistral",
        openai_api_key="not-needed",
        openai_api_base="http://localhost:11434/v1",
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
