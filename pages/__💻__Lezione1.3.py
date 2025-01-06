import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 1.3", page_icon="💻", layout="wide")

st.write("# Lezione 1.3: File e cartelle: organizzazione e gestione")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/Organizzare-File.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Comprendere cosa sono file e cartelle
            - Imparare a organizzare i documenti
            - Acquisire competenze base nella gestione dei file

            ## Contenuti

            ### 1. Concetti Base

            #### File
            - Cos'è un file: unità base di archiviazione delle informazioni
            - Tipi comuni di file:
                - Documenti (.doc, .docx, .pdf)
                - Immagini (.jpg, .png)
                - Video (.mp4)
                - Audio (.mp3)
            - Come riconoscere i tipi di file dalle icone

            #### Cartelle
            - Cos'è una cartella: contenitore per organizzare i file
            - Cartelle di sistema predefinite:
                - Documenti
                - Immagini
                - Download
                - Desktop

            ### 2. Operazioni Base

            #### Gestione File e Cartelle
            - Creare una nuova cartella
            - Rinominare file e cartelle
            - Spostare file e cartelle
            - Copiare file e cartelle
            - Eliminare file e cartelle
            - Recuperare file dal Cestino

            #### Esplorazione File
            - Aprire Esplora File
            - Navigare tra le cartelle
            - Utilizzare la barra degli indirizzi
            - Visualizzare dettagli dei file
            - Ordinare e filtrare i file

            ### 3. Organizzazione Efficiente
            - Creare una struttura logica delle cartelle
            - Dare nomi significativi ai file
            - Utilizzare sottocartelle per categorie
            - Mantenere il desktop ordinato

            ## Esercizi Pratici
            1. Crea una struttura di cartelle per organizzare i tuoi documenti
            2. Esercitati con le operazioni di base:
                - Crea alcune cartelle
                - Sposta e copia dei file
                - Rinomina file e cartelle
                - Elimina e recupera dal cestino
            3. Organizza il desktop creando cartelle appropriate

            ## Verifica Apprendimento
            - Sai creare e gestire cartelle?
            - Comprendi la differenza tra spostare e copiare?
            - Sai come recuperare file eliminati?
            - Riesci a mantenere i tuoi documenti organizzati?
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
