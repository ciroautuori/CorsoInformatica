import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 3.3", page_icon="💻", layout="wide")

st.write("# Lezione 3.3: Gestione PDF: visualizzazione e modifiche semplici")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/PDF.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Comprendere cos'è un file PDF
            - Imparare a visualizzare e navigare nei PDF
            - Acquisire competenze base per la modifica dei PDF
            - Conoscere gli strumenti principali per la gestione dei PDF

            ## Contenuti

            ### 1. Introduzione ai PDF

            #### Cos'è un PDF
            - Definizione di PDF (Portable Document Format)
            - Vantaggi del formato PDF
            - Differenze tra PDF e altri formati
            - Quando utilizzare i PDF

            #### Strumenti necessari
            - Adobe Acrobat Reader (gratuito)
            - Altri lettori PDF
            - Differenze tra versione gratuita e professionale
            - Installazione e configurazione base

            ### 2. Visualizzazione PDF

            #### Funzioni base di lettura
            - Aprire un PDF
            - Navigare tra le pagine
            - Zoom e visualizzazione
            - Ricerca nel documento
            - Rotazione pagine

            #### Strumenti di navigazione
            - Utilizzo dei segnalibri
            - Miniature delle pagine
            - Visualizzazione a schermo intero
            - Modalità di lettura

            ### 3. Operazioni Base

            #### Gestione del documento
            - Salvare PDF
            - Stampare PDF
            - Copiare testo da PDF
            - Effettuare screenshot
            - Condividere PDF

            #### Annotazioni semplici
            - Evidenziare testo
            - Aggiungere note
            - Inserire commenti
            - Utilizzare timbri
            - Disegnare sul PDF

            ### 4. Modifiche Base

            #### Operazioni comuni
            - Unire PDF
            - Estrarre pagine
            - Ruotare pagine
            - Riordinare pagine
            - Comprimere PDF

            #### Conversione
            - Da Word a PDF
            - Da PDF a Word
            - Da immagini a PDF
            - Limitazioni delle conversioni

            ## Esercizi Pratici

            1. Gestione base:
            - Apri e naviga in un PDF lungo
            - Usa gli strumenti di zoom
            - Cerca parole specifiche
            - Copia parti di testo

            2. Annotazioni:
            - Evidenzia parti importanti
            - Aggiungi commenti
            - Inserisci note
            - Salva le modifiche

            3. Progetto pratico:
            - Gestisci un documento PDF:
                - Unisci più PDF
                - Estrai pagine specifiche
                - Aggiungi annotazioni
                - Condividi il risultato

            ## Verifica Apprendimento
            - Sai aprire e navigare nei PDF?
            - Riesci a utilizzare gli strumenti di annotazione?
            - Comprendi le operazioni base di modifica?
            - Sai gestire la conversione dei documenti?

            ## Suggerimenti Pratici
            - Mantieni aggiornato il software PDF
            - Usa le scorciatoie da tastiera
            - Salva spesso durante le modifiche
            - Verifica sempre il risultato finale
                        
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
