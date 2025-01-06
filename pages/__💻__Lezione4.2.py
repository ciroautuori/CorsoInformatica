import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 4.2", page_icon="💻", layout="wide")

st.write("# Lezione 4.2: Cloud storage e condivisione file")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/CondivisioneFile.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Comprendere cos'è il cloud storage
            - Imparare a utilizzare i servizi cloud più comuni
            - Gestire la condivisione sicura dei file
            - Organizzare i documenti nel cloud

            ## Contenuti

            ### 1. Introduzione al Cloud Storage

            #### Cos'è il Cloud
            - Definizione di cloud storage
            - Vantaggi del cloud
            - Differenze con storage locale
            - Principali servizi disponibili:
            - Google Drive
            - OneDrive
            - Dropbox

            #### Sicurezza e Privacy
            - Password sicure
            - Autenticazione a due fattori
            - Crittografia dei dati
            - Backup automatico

            ### 2. Utilizzo Base

            #### Configurazione Iniziale
            - Creazione account
            - Installazione app desktop
            - Sincronizzazione dispositivi
            - Gestione spazio disponibile

            #### Operazioni Fondamentali
            - Caricare file e cartelle
            - Scaricare contenuti
            - Organizzare documenti
            - Sincronizzare dati

            ### 3. Condivisione e Collaborazione

            #### Condivisione File
            - Link di condivisione
            - Permessi di accesso
            - Scadenza condivisioni
            - Revoca accessi

            #### Lavoro Collaborativo
            - Modifica simultanea
            - Commenti e suggerimenti
            - Cronologia versioni
            - Ripristino file

            ### 4. Gestione Avanzata

            #### Organizzazione Efficiente
            - Struttura cartelle
            - Nomenclatura file
            - Tag e metadati
            - Ricerca avanzata

            #### Funzionalità Extra
            - Backup automatico
            - Accesso offline
            - Integrazione app
            - Gestione spazio

            ## Esercizi Pratici

            1. Configurazione base:
            - Crea un account cloud
            - Installa l'app desktop
            - Configura la sincronizzazione
            - Organizza lo spazio

            2. Gestione file:
            - Carica documenti vari
            - Crea struttura cartelle
            - Sincronizza dispositivi
            - Gestisci versioni

            3. Condivisione:
            - Condividi file con altri
            - Imposta permessi
            - Collabora su documenti
            - Gestisci accessi

            ## Verifica Apprendimento
            - Sai utilizzare il cloud storage?
            - Gestisci correttamente le condivisioni?
            - Mantieni organizzati i file?
            - Comprendi le misure di sicurezza?

            ## Suggerimenti Pratici
            - Mantieni una struttura ordinata
            - Fai backup regolari
            - Controlla periodicamente le condivisioni
            - Usa password sicure
                        
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
