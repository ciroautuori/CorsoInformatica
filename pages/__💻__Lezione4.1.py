import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 4.1", page_icon="💻", layout="wide")

st.write("# Lezione 4.1: ChatGPT: introduzione e utilizzo base")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/CGPT.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Comprendere cos'è ChatGPT e come funziona
            - Imparare a utilizzare ChatGPT in modo efficace
            - Conoscere i limiti e le potenzialità dello strumento
            - Sviluppare buone pratiche di utilizzo

            ## Contenuti

            ### 1. Introduzione a ChatGPT

            #### Cos'è ChatGPT
            - Definizione di intelligenza artificiale conversazionale
            - Come funziona ChatGPT
            - Differenze con altri strumenti
            - Casi d'uso comuni

            #### Accesso e Configurazione
            - Creazione account OpenAI
            - Versioni disponibili (gratuita vs Plus)
            - Interfaccia web
            - App mobile

            ### 2. Utilizzo Base

            #### Principi Fondamentali
            - Come formulare le domande
            - Importanza del contesto
            - Chiarezza nelle richieste
            - Feedback e iterazioni

            #### Tipi di Interazione
            - Domande e risposte
            - Richieste di spiegazioni
            - Correzioni e revisioni
            - Traduzioni
            - Riassunti

            ### 3. Applicazioni Pratiche

            #### Scrittura e Editing
            - Correzione grammaticale
            - Miglioramento testi
            - Generazione contenuti
            - Stili di scrittura

            #### Supporto Quotidiano
            - Ricerca informazioni
            - Risoluzione problemi
            - Consigli pratici
            - Organizzazione attività

            ### 4. Buone Pratiche

            #### Uso Efficace
            - Essere specifici nelle richieste
            - Fornire contesto adeguato
            - Verificare le informazioni
            - Iterare le domande

            #### Limiti e Precauzioni
            - Verifica delle fonti
            - Privacy e dati sensibili
            - Limiti temporali
            - Possibili errori

            ## Esercizi Pratici

            1. Prime interazioni:
            - Presentati a ChatGPT
            - Fai domande semplici
            - Sperimenta diversi tipi di richieste
            - Osserva le risposte

            2. Utilizzo guidato:
            - Chiedi spiegazioni su un argomento
            - Fai correggere un testo
            - Richiedi un riassunto
            - Prova una traduzione

            3. Progetto pratico:
            - Usa ChatGPT per:
                - Pianificare un'attività
                - Risolvere un problema
                - Creare un contenuto
                - Ottenere feedback

            ## Verifica Apprendimento
            - Sai interagire efficacemente con ChatGPT?
            - Comprendi i limiti dello strumento?
            - Riesci a ottenere risposte utili?
            - Sai come verificare le informazioni?

            ## Suggerimenti Pratici
            - Mantieni le richieste chiare e concise
            - Specifica sempre il contesto
            - Verifica le informazioni importanti
            - Usa ChatGPT come supporto, non come fonte unica
                        
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
