import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 3.2", page_icon="💻", layout="wide")

st.write("# Lezione 3.2: Microsoft Excel - Fogli di calcolo introduzione")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/Excel.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """  
            ## Obiettivi della lezione
            - Comprendere l'interfaccia di Microsoft Excel
            - Imparare le funzioni base dei fogli di calcolo
            - Creare tabelle e formule semplici

            ## Contenuti

            ### 1. Introduzione a Microsoft Excel

            #### L'interfaccia di Excel
            - La griglia del foglio di calcolo
            - Righe e colonne
            - Celle e riferimenti
            - Barra della formula
            - Fogli di lavoro

            #### Concetti base
            - Differenza tra testo e numeri
            - Formattazione delle celle
            - Larghezza colonne e altezza righe
            - Navigazione nel foglio

            ### 2. Gestione Dati

            #### Inserimento dati
            - Digitazione diretta
            - Serie di dati automatiche
            - Copia e incolla
            - Riempimento automatico
            - Formati numerici

            #### Formattazione
            - Allineamento
            - Bordi e sfondi
            - Formati numerici personalizzati
            - Stili celle predefiniti
            - Unione celle

            ### 3. Formule Base

            #### Operazioni matematiche
            - Addizione (+)
            - Sottrazione (-)
            - Moltiplicazione (*)
            - Divisione (/)
            - Percentuali

            #### Funzioni semplici
            - SOMMA
            - MEDIA
            - MAX
            - MIN
            - CONTA.NUMERI

            ### 4. Organizzazione

            #### Gestione fogli
            - Rinominare fogli
            - Spostare e copiare fogli
            - Colorare le schede
            - Collegamenti tra fogli

            #### Stampa
            - Impostazione area di stampa
            - Anteprima di stampa
            - Intestazioni
            - Adattamento alla pagina

            ## Esercizi Pratici

            1. Creazione tabella base:
            - Crea una tabella spese mensili
            - Inserisci intestazioni
            - Formatta numeri come valuta
            - Calcola totali

            2. Calcoli con formule:
            - Usa operazioni matematiche base
            - Applica funzioni SOMMA e MEDIA
            - Copia formule
            - Verifica risultati

            3. Progetto pratico:
            - Crea un registro spese con:
                - Categorie di spesa
                - Totali mensili
                - Grafici semplici
                - Formattazione professionale

            ## Verifica Apprendimento
            - Sai inserire e formattare dati?
            - Comprendi l'uso delle formule base?
            - Riesci a organizzare un foglio di lavoro?
            - Sai preparare un documento per la stampa?

            ## Suggerimenti Pratici
            - Usa il tasto F2 per modificare le celle
            - Impara i tasti rapidi più comuni
            - Verifica sempre le formule
            - Mantieni i fogli ordinati e ben strutturati
                        
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
