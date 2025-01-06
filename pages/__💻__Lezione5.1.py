import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 5.1", page_icon="💻", layout="wide")

st.write("# Lezione 5.1: Password sicure e gestione")
st.image("./src/img/banner.jpg", width=None)
st.audio("./src/audio/PasswordSicure.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Comprendere l'importanza delle password sicure
            - Imparare a creare e gestire password efficaci
            - Conoscere i rischi delle password deboli
            - Utilizzare un password manager

            ## Contenuti

            ### 1. Fondamenti della Sicurezza Password

            #### Caratteristiche Password Sicura
            - Lunghezza minima (almeno 12 caratteri)
            - Combinazione di caratteri:
            - Lettere maiuscole e minuscole
            - Numeri
            - Simboli speciali
            - Evitare informazioni personali
            - Non usare parole comuni

            #### Errori Comuni
            - Password troppo semplici
            - Riutilizzo delle password
            - Condivisione password
            - Memorizzazione non sicura

            ### 2. Creazione Password Sicure

            #### Metodi di Creazione
            - Frasi passphrase
            - Generatori di password
            - Tecniche mnemoniche
            - Pattern personalizzati

            #### Gestione Diversificata
            - Password diverse per ogni servizio
            - Prioritizzazione per importanza
            - Rotazione periodica
            - Recupero password

            ### 3. Password Manager

            #### Introduzione
            - Cos'è un password manager
            - Vantaggi dell'utilizzo
            - Principali software disponibili:
            - LastPass
            - Bitwarden
            - 1Password

            #### Configurazione e Uso
            - Installazione software
            - Creazione master password
            - Importazione password esistenti
            - Generazione nuove password
            - Sincronizzazione dispositivi

            ### 4. Sicurezza Avanzata

            #### Autenticazione a Due Fattori (2FA)
            - Cos'è il 2FA
            - Metodi disponibili:
            - SMS
            - App authenticator
            - Chiavi di sicurezza
            - Configurazione su servizi principali

            #### Backup e Recupero
            - Backup password manager
            - Procedure di recupero
            - Documentazione sicura
            - Piano di emergenza

            ## Esercizi Pratici

            1. Creazione password:
            - Crea password sicure
            - Usa tecniche mnemoniche
            - Verifica la robustezza
            - Documenta in modo sicuro

            2. Password Manager:
            - Installa un password manager
            - Configura le impostazioni base
            - Importa password esistenti
            - Genera nuove password

            3. Sicurezza avanzata:
            - Attiva 2FA sui servizi principali
            - Configura app authenticator
            - Crea backup sicuri
            - Testa procedure di recupero

            ## Verifica Apprendimento
            - Sai creare password sicure?
            - Utilizzi correttamente un password manager?
            - Hai attivato l'autenticazione a due fattori?
            - Gestisci in modo sicuro i backup?

            ## Suggerimenti Pratici
            - Cambia subito le password deboli
            - Usa sempre password uniche
            - Attiva 2FA dove possibile
            - Mantieni aggiornato il password manager
                        
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
