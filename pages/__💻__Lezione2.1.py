import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 2.1", page_icon="💻", layout="wide")

st.write("# Lezione 2.1: Navigare su Internet in sicurezza")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/NavigareSicurezza.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Comprendere cos'è Internet e come funziona
            - Imparare a utilizzare un browser web
            - Acquisire le basi della sicurezza online

            ## Contenuti

            ### 1. Introduzione a Internet

            #### Cos'è Internet
            - La rete globale di computer
            - Come ci si connette a Internet
            - Il ruolo del browser web

            #### Browser Web Comuni
            - Google Chrome
            - Microsoft Edge
            - Mozilla Firefox
            - Come scegliere il browser più adatto

            ### 2. Navigazione Base

            #### Utilizzo del Browser
            - La barra degli indirizzi
            - I pulsanti di navigazione (Avanti/Indietro)
            - Le schede (tab) del browser
            - I preferiti/segnalibri
            - La cronologia di navigazione

            #### Ricerche su Internet
            - Utilizzare i motori di ricerca
            - Tecniche di ricerca efficace
            - Valutare l'affidabilità dei risultati

            ### 3. Sicurezza Online

            #### Rischi comuni
            - Siti web non sicuri
            - Download pericolosi
            - Pubblicità ingannevole
            - Tentativi di phishing

            #### Pratiche di Sicurezza
            - Verificare l'HTTPS (lucchetto verde)
            - Non fornire dati personali
            - Evitare download sospetti
            - Riconoscere siti affidabili

            ### 4. Funzionalità Avanzate
            - Salvare pagine web
            - Stampare pagine web
            - Zoom e personalizzazione vista
            - Gestione download

            ## Esercizi Pratici
            1. Configurazione del browser:
            - Imposta la pagina iniziale
            - Crea alcuni segnalibri
            - Personalizza la barra degli strumenti

            2. Ricerche guidate:
            - Cerca informazioni specifiche
            - Valuta l'affidabilità delle fonti
            - Salva pagine interessanti nei preferiti

            3. Verifica della sicurezza:
            - Identifica siti sicuri e non sicuri
            - Riconosci tentativi di phishing
            - Pratica la navigazione sicura

            ## Verifica Apprendimento
            - Sai utilizzare le funzioni base del browser?
            - Riconosci un sito web sicuro?
            - Sai effettuare ricerche efficaci?
            - Comprendi i rischi della navigazione?
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
