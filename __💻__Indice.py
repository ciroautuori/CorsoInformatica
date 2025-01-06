import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(
    page_title="Indice",
    page_icon="👋",
    layout="wide"
)

st.write("# Corso Base di Informatica e Competenze Digitali")
st.image("./src/img/banner.jpg", width=None)

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:

    st.markdown("## Modulo 1: Fondamenti del Computer")

    st.checkbox(
        "Lezione 1.1: Cos'è un computer: componenti base e loro funzioni")

    st.checkbox(
        "Lezione 1.2: Il sistema operativo: Windows e le sue funzionalità principali")

    st.checkbox(
        "Lezione 1.3: File e cartelle: organizzazione e gestione")

    st.checkbox(
        "Lezione 1.4: Esercitazioni pratiche Modulo 1")

    st.markdown("## Modulo 2: Internet e Comunicazione")

    st.checkbox(
        "Lezione 2.1: Navigare su Internet in sicurezza")

    st.checkbox(
        "Lezione 2.2: Email: configurazione e utilizzo")

    st.checkbox(
        "Lezione 2.3: PEC: cos'è e come utilizzarla")

    st.checkbox(
        "Lezione 2.4: Esercitazioni pratiche Modulo 2")

    st.markdown("## Modulo 3: Microsoft Office Base")

    st.checkbox(
        "Lezione 3.1: Microsoft Word - Creazione documenti base")

    st.checkbox(
        "Lezione 3.2: Microsoft Excel - Fogli di calcolo introduzione")

    st.checkbox(
        "Lezione 3.3: Gestione PDF: visualizzazione e modifiche semplici")

    st.checkbox(
        "Lezione 3.4: Esercitazioni pratiche Modulo 3")

    st.markdown("## Modulo 4: Strumenti Digitali Avanzati")

    st.checkbox(
        "Lezione 4.1: ChatGPT: introduzione e utilizzo base")

    st.checkbox(
        "Lezione 4.2: Cloud storage e condivisione file")

    st.checkbox(
        "Lezione 4.3: Calendario digitale e gestione appuntamenti")

    st.checkbox(
        "Lezione 4.4: Esercitazioni pratiche Modulo 4")

    st.markdown("## Modulo 5: Sicurezza Digitale")

    st.checkbox(
        "Lezione 5.1: Password sicure e gestione")

    st.checkbox(
        "Lezione 5.2: Riconoscere e evitare truffe online")

    st.checkbox(
        "Lezione 5.3: Backup dei dati")

    st.checkbox(
        "Lezione 5.4: Esercitazioni pratiche Modulo 5")

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
