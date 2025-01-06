import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Riepilogo", page_icon="💻", layout="wide")

st.write("# Riepilogo Finale: Corso Base di Informatica e Competenze Digitali")
st.image("./src/img/banner.jpg", width=None)

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
               

            ## Panoramica del Corso
            Questo corso ha fornito le competenze fondamentali per utilizzare il computer e gli strumenti digitali in modo efficace e sicuro.

            ## Moduli Completati

            ### Modulo 1: Fondamenti del Computer
            - **Componenti base e funzioni**
            - Hardware e periferiche
            - Sistema operativo Windows
            - Gestione file e cartelle
            
            - **Competenze acquisite**
            - Utilizzo base del computer
            - Navigazione nel sistema operativo
            - Organizzazione dei documenti

            ### Modulo 2: Internet e Comunicazione
            - **Navigazione e sicurezza web**
            - Utilizzo dei browser
            - Ricerche efficaci
            - Sicurezza online

            - **Gestione email e PEC**
            - Configurazione account
            - Gestione messaggi
            - Comunicazioni certificate

            ### Modulo 3: Microsoft Office Base
            - **Word**
            - Creazione documenti
            - Formattazione testo
            - Elementi avanzati

            - **Excel**
            - Fogli di calcolo
            - Formule base
            - Organizzazione dati

            - **Gestione PDF**
            - Visualizzazione
            - Modifiche base
            - Conversione documenti

            ### Modulo 4: Strumenti Digitali Avanzati
            - **ChatGPT**
            - Utilizzo base
            - Prompt efficaci
            - Applicazioni pratiche

            - **Cloud e Calendario**
            - Storage online
            - Condivisione file
            - Gestione appuntamenti

            ### Modulo 5: Sicurezza Digitale
            - **Protezione dati**
            - Password sicure
            - Prevenzione truffe
            - Backup sistematico

            ## Competenze Chiave Sviluppate
            1. Autonomia nell'uso del computer
            2. Comunicazione digitale efficace
            3. Gestione documenti e dati
            4. Sicurezza informatica base
            5. Produttività digitale

            ## Prossimi Passi Consigliati
            - Pratica regolare delle competenze acquisite
            - Approfondimento degli argomenti di maggior interesse
            - Mantenimento aggiornato delle misure di sicurezza
            - Esplorazione di strumenti avanzati

            ## Risorse per Continuare
            - Documentazione ufficiale dei software
            - Tutorial online
            - Comunità di supporto
            - Aggiornamenti periodici

            ## Conclusione
            Il completamento di questo corso rappresenta il primo passo nel mondo digitale. Le competenze acquisite forniscono una base solida per:
            - Utilizzo efficiente del computer
            - Comunicazione digitale sicura
            - Gestione professionale dei documenti
            - Protezione dei dati personali
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
