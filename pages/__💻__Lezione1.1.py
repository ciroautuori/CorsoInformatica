import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 1.1", page_icon="💻", layout="wide")

st.write("# Lezione 1.1: Cos'è un computer: componenti base e loro funzioni")
st.image("./src/img/banner.jpg", width=None)
# st.video()
st.audio("./src/audio/Componenti-Fondamentali.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """   
            ## Obiettivi della lezione
            - Comprendere cos'è un computer
            - Identificare i componenti principali di un computer
            - Capire la funzione base di ogni componente

            ## Contenuti

            ### 1. Cos'è un computer?
            Il computer è una macchina elettronica che elabora informazioni seguendo delle istruzioni (programmi).

            ### 2. Componenti principali:

            #### Monitor
            - È lo schermo dove vediamo le informazioni
            - Può essere integrato (laptop) o separato (desktop)

            #### Tastiera
            - Serve per inserire testo e comandi
            - Ha tasti alfanumerici e tasti speciali

            #### Mouse
            - Permette di muovere il cursore sullo schermo
            - Ha pulsanti per selezionare e attivare funzioni

            #### Unità centrale (CPU)
            - È il "cervello" del computer
            - Elabora tutte le informazioni

            #### Memoria (RAM)
            - Memoria temporanea per i programmi in uso
            - Si cancella quando spegniamo il computer

            #### Disco rigido
            - Memoria permanente
            - Conserva file e programmi anche da spento

            ## Esercizio pratico
            1. Identifica questi componenti sul tuo computer
            2. Prova ad accendere e spegnere il computer correttamente
            3. Usa il mouse per muovere il cursore sullo schermo

            ## Verifica apprendimento
            - Sai identificare i componenti principali?
            - Comprendi la differenza tra RAM e disco rigido?
            - Sai accendere e spegnere correttamente il computer?
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
