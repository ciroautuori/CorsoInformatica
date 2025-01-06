import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 2.2", page_icon="💻", layout="wide")

st.write("# Lezione 2.2: Email: configurazione e utilizzo")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/Email.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
         ## Obiettivi della lezione
         - Comprendere cos'è un'email e come funziona
         - Creare e configurare un account email
         - Imparare a gestire la posta elettronica in modo efficace

         ## Contenuti

         ### 1. Introduzione all'Email

         #### Cos'è l'Email
         - Posta elettronica: definizione e funzionamento
         - Struttura di un indirizzo email (nome@dominio.com)
         - Principali servizi email (Gmail, Outlook, etc.)

         #### Elementi di un'Email
         - Destinatario (A:)
         - Copia Carbone (CC:)
         - Copia Carbone Nascosta (CCN:)
         - Oggetto
         - Corpo del messaggio
         - Allegati

         ### 2. Creazione Account Email

         #### Configurazione Iniziale
         - Scegliere un servizio email
         - Creare un indirizzo professionale
         - Impostare password sicura
         - Configurare il profilo personale

         #### Impostazioni Base
         - Firma email
         - Risposta automatica
         - Organizzazione cartelle
         - Filtri spam

         ### 3. Utilizzo Quotidiano

         #### Gestione Email
         - Scrivere nuove email
         - Rispondere ai messaggi
         - Inoltrare email
         - Gestire allegati
         - Come allegare file
         - Limiti dimensioni
         - Formati supportati

         #### Organizzazione
         - Creare cartelle
         - Utilizzare etichette/tag
         - Archiviare messaggi
         - Gestire lo spam

         ### 4. Sicurezza Email

         #### Pratiche Sicure
         - Riconoscere email sospette
         - Evitare il phishing
         - Gestire lo spam
         - Password sicure

         ## Esercizi Pratici
         1. Configurazione account:
            - Crea un nuovo account email
            - Imposta il profilo personale
            - Configura la firma

         2. Gestione base:
            - Invia un'email con allegato
            - Rispondi a un'email
            - Inoltra un messaggio
            - Organizza in cartelle

         3. Sicurezza:
            - Identifica email sospette
            - Configura filtri anti-spam
            - Crea password sicura

         ## Verifica Apprendimento
         - Sai creare e gestire un account email?
         - Comprendi la differenza tra CC e CCN?
         - Sai gestire gli allegati?
         - Riconosci le email sospette?
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
