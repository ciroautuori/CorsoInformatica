import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 5.4", page_icon="💻", layout="wide")

st.write("# # Lezione 5.4: Esercitazioni pratiche Modulo 5")
st.image("./src/img/banner.jpg", width=None)

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """ 
            ## Obiettivi della lezione
            - Consolidare le competenze di sicurezza digitale
            - Mettere in pratica le misure di protezione
            - Verificare la comprensione delle procedure di sicurezza
            - Creare un ambiente digitale sicuro e protetto

            ## Contenuti

            ### 1. Sicurezza Password

            #### Progetto 1: Sistema Password Sicuro
            1. Implementazione completa:
            - Audit password esistenti
            - Creazione nuove password sicure
            - Configurazione password manager
            - Attivazione 2FA su tutti i servizi

            2. Documentazione:
            - Piano di recupero password
            - Procedure di emergenza
            - Registro accessi
            - Backup credenziali

            ### 2. Protezione dalle Truffe

            #### Progetto 2: Simulazione Scenari
            1. Analisi casi reali:
            - Email di phishing
            - Siti web fraudolenti
            - Messaggi sospetti
            - Chiamate truffa

            2. Procedure di risposta:
            - Identificazione minacce
            - Documentazione tentativi
            - Segnalazione incidenti
            - Misure preventive

            ### 3. Sistema di Backup

            #### Progetto 3: Implementazione Backup Completo
            1. Configurazione sistema:
            - Backup locale automatico
            - Sync cloud
            - Copie offline
            - Verifica periodica

            2. Piano di recupero:
            - Procedure di ripristino
            - Test di recupero
            - Documentazione processo
            - Aggiornamento procedure

            ### 4. Challenge Finale

            #### Simulazione Sicurezza Completa
            1. Scenario integrato:
            - Gestione password
            - Prevenzione truffe
            - Backup dati
            - Risposta incidenti

            2. Valutazione rischi:
            - Analisi vulnerabilità
            - Misure preventive
            - Piano d'azione
            - Monitoraggio continuo

            ## Esercizi Pratici

            1. Security Check Completo:
            - Verifica tutte le password
            - Controlla impostazioni sicurezza
            - Testa backup esistenti
            - Documenta configurazioni

            2. Simulazione Attacchi:
            - Riconosci tentativi di phishing
            - Gestisci situazioni sospette
            - Applica procedure sicurezza
            - Esegui recovery plan

            3. Ottimizzazione Sistema:
            - Migliora misure sicurezza
            - Automatizza procedure
            - Aggiorna documentazione
            - Pianifica manutenzione

            ## Verifica Competenze
            - Gestisci efficacemente la sicurezza?
            - Riconosci e previeni le minacce?
            - Mantieni backup aggiornati?
            - Applichi le procedure corrette?

""")

# Checklist Finale Modulo 4
st.checkbox("Sistema password sicuro")
st.checkbox("Protezione da truffe attiva")
st.checkbox("Backup funzionante")
st.checkbox("Procedure documentate")
st.checkbox("Monitoraggio attivo")
st.checkbox("Piano emergenza testato")

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
