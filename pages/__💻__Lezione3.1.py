import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 3.1", page_icon="💻", layout="wide")

st.write("# Lezione 3.1: Microsoft Word - Creazione documenti base")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/Word.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """  
            ## Obiettivi della lezione
            - Familiarizzare con l'interfaccia di Microsoft Word
            - Imparare le funzioni base di formattazione del testo
            - Creare e salvare documenti semplici

            ## Contenuti

            ### 1. Introduzione a Microsoft Word

            #### L'interfaccia di Word
            - La barra multifunzione (Ribbon)
            - Barra di accesso rapido
            - Righello e guide
            - Visualizzazione del documento

            #### Operazioni base
            - Creare un nuovo documento
            - Aprire documenti esistenti
            - Salvare documenti
            - Differenza tra .doc e .docx

            ### 2. Gestione del Testo

            #### Formattazione base
            - Selezionare il testo
            - Modificare il carattere
            - Cambiare dimensione
            - Applicare stili (grassetto, corsivo, sottolineato)
            - Colore del testo

            #### Paragrafi
            - Allineamento (sinistra, centro, destra, giustificato)
            - Interlinea
            - Spaziatura prima e dopo
            - Rientri
            - Elenchi puntati e numerati

            ### 3. Strumenti di Editing

            #### Funzioni essenziali
            - Taglia, copia e incolla
            - Annulla e ripeti
            - Trova e sostituisci
            - Controllo ortografico
            - Conteggio parole

            #### Layout pagina
            - Margini
            - Orientamento pagina
            - Dimensione foglio
            - Interruzioni di pagina

            ### 4. Elementi Aggiuntivi

            #### Arricchire il documento
            - Inserire immagini
            - Aggiungere tabelle semplici
            - Bordi e sfondi
            - Intestazione e piè di pagina

            ## Esercizi Pratici

            1. Creazione documento base:
            - Crea un nuovo documento
            - Scrivi un breve testo
            - Applica formattazioni base
            - Salva il documento

            2. Formattazione avanzata:
            - Crea un documento con diversi stili
            - Inserisci elenchi puntati e numerati
            - Aggiungi un'immagine
            - Crea una tabella semplice

            3. Esercizio completo:
            - Crea una lettera formale con:
                - Intestazione
                - Corpo del testo formattato
                - Firma
                - Piè di pagina

            ## Verifica Apprendimento
            - Sai creare e salvare documenti?
            - Padroneggi le formattazioni base?
            - Sai gestire il layout della pagina?
            - Riesci a inserire elementi aggiuntivi?

            ## Suggerimenti Pratici
            - Usa i tasti rapidi per le operazioni frequenti
            - Salva spesso il documento
            - Mantieni una formattazione coerente
            - Utilizza gli strumenti di controllo ortografico
                        
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
