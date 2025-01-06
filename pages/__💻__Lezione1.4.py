import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 1.4", page_icon="💻", layout="wide")

st.write("# Lezione 1.4: Esercitazioni pratiche Modulo 1")
st.image("./src/img/banner.jpg", width=None)
# st.audio("./src/audio/Windows.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Consolidare le competenze acquisite nel Modulo 1
            - Mettere in pratica le conoscenze in scenari reali
            - Verificare la comprensione generale degli argomenti

            ## Esercitazioni

            ### Esercizio 1: Componenti del Computer
            1. Identifica e elenca tutti i componenti del tuo computer
            2. Spiega la funzione di ciascun componente
            3. Crea un documento con l'elenco dei componenti e le loro funzioni

            ### Esercizio 2: Windows e Desktop
            1. Personalizza il desktop:
            - Cambia lo sfondo
            - Organizza le icone
            - Modifica la barra delle applicazioni
            2. Pratica con le finestre:
            - Apri 3 programmi diversi
            - Disponi le finestre affiancate
            - Passa da un programma all'altro

            ### Esercizio 3: Gestione File
            1. Crea la seguente struttura di cartelle:
            ```
            Documenti Personali/
            ├── Documenti Importanti/
            ├── Foto/
            │   ├── Famiglia/
            │   └── Vacanze/
            └── Lavoro/
                ├── Progetti/
                └── Contratti/
            ```
            2. Sposta alcuni file nelle cartelle appropriate
            3. Rinomina alcuni file seguendo una convenzione logica
            4. Crea copie di backup dei documenti importanti

            ## Verifica Finale del Modulo
            - Sai gestire autonomamente il computer?
            - Padroneggi l'interfaccia di Windows?
            - Sei in grado di organizzare file e cartelle?
            - Ti senti sicuro/a nell'utilizzo delle funzioni base?

            ## Progetto Pratico
            Crea una presentazione semplice che illustri:
            1. I componenti principali del tuo computer
            2. Le funzioni di Windows che usi più spesso
            3. La tua organizzazione di file e cartelle
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
