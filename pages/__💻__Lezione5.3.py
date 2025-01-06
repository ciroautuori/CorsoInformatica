import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 5.3", page_icon="💻", layout="wide")

st.write("# Lezione 5.3: Backup dei dati")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/BackupDati.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Comprendere l'importanza del backup
            - Imparare diverse strategie di backup
            - Implementare un sistema di backup efficace
            - Gestire il recupero dei dati

            ## Contenuti

            ### 1. Fondamenti del Backup

            #### Perché fare Backup
            - Protezione da perdita dati
            - Difesa da malware e virus
            - Recupero da errori umani
            - Conservazione storica
            - Conformità normativa

            #### Tipi di Backup
            - Backup completo
            - Backup incrementale
            - Backup differenziale
            - Backup in tempo reale
            - Backup cloud

            ### 2. Strategie di Backup

            #### Regola 3-2-1
            - 3 copie dei dati
            - 2 tipi di supporti diversi
            - 1 copia fuori sede
            - Implementazione pratica
            - Verifica periodica

            #### Supporti di Backup
            - Dischi esterni
            - Chiavette USB
            - NAS (Network Attached Storage)
            - Servizi cloud
            - Nastri magnetici (ambiente professionale)

            ### 3. Implementazione

            #### Backup Locale
            - Configurazione Windows Backup
            - Software di backup dedicati
            - Pianificazione automatica
            - Verifica dei backup
            - Test di ripristino

            #### Backup Cloud
            - Servizi disponibili
            - Configurazione sync
            - Backup automatico
            - Crittografia
            - Gestione spazio

            ### 4. Recupero Dati

            #### Procedure di Ripristino
            - Verifica integrità backup
            - Selezione dati da ripristinare
            - Processo di recupero
            - Test post-ripristino
            - Documentazione

            #### Gestione Emergenze
            - Piano di disaster recovery
            - Priorità di ripristino
            - Tempi di recupero
            - Test periodici
            - Aggiornamento procedure

            ## Esercizi Pratici

            1. Configurazione backup:
            - Imposta backup Windows
            - Configura backup cloud
            - Pianifica backup automatici
            - Verifica completamento

            2. Gestione backup:
            - Organizza file da backuppare
            - Implementa regola 3-2-1
            - Testa backup incrementali
            - Documenta procedure

            3. Test di ripristino:
            - Simula perdita dati
            - Esegui recupero file
            - Verifica integrità
            - Ottimizza processo

            ## Verifica Apprendimento
            - Hai implementato un sistema di backup?
            - Comprendi i diversi tipi di backup?
            - Sai recuperare i dati dal backup?
            - Mantieni backup aggiornati?

            ## Suggerimenti Pratici
            - Backup regolari e automatici
            - Verifica periodica dei backup
            - Conserva backup offline
            - Documenta le procedure         
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
