import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 1.2", page_icon="💻", layout="wide")

st.write("# Lezione 1.2: Il sistema operativo Windows e le sue funzionalità principali")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/Windows.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """    
            ## Obiettivi della lezione
            - Comprendere cos'è un sistema operativo
            - Familiarizzare con l'interfaccia di Windows
            - Imparare le funzioni base di Windows

            ## Contenuti

            ### 1. Il Sistema Operativo
            - È il software principale che gestisce il computer
            - Permette l'interazione tra utente e computer
            - Windows è il sistema operativo più diffuso

            ### 2. Il Desktop di Windows
            #### La Schermata Iniziale
            - Il Desktop è la schermata principale
            - Le icone rappresentano programmi o file
            - Lo sfondo può essere personalizzato

            #### La Barra delle Applicazioni
            - Si trova in basso sullo schermo
            - Contiene:
            - Pulsante Start (logo Windows)
            - Programmi aperti
            - Area di notifica (orologio, volume, ecc.)

            ### 3. Funzioni Base

            #### Il Menu Start
            - Accesso a tutti i programmi
            - Spegnimento/Riavvio del computer
            - Ricerca rapida

            #### Le Finestre
            - Come aprire una finestra
            - Come ridurre a icona
            - Come ingrandire/ripristinare
            - Come chiudere
            - Come spostare e ridimensionare

            #### Multitasking
            - Lavorare con più finestre
            - Passare da un programma all'altro
            - Visualizzare finestre affiancate

            ## Esercizi Pratici
            1. Apri il Menu Start e esplora le sue sezioni
            2. Prova ad aprire, spostare e ridimensionare alcune finestre
            3. Esercitati nel passaggio tra diverse applicazioni
            4. Personalizza lo sfondo del Desktop

            ## Verifica Apprendimento
            - Sai utilizzare il Menu Start?
            - Riesci a gestire più finestre contemporaneamente?
            - Sai come spegnere correttamente il computer?
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
