import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 4.4", page_icon="💻", layout="wide")

st.write("# Lezione 4.4: Esercitazioni pratiche Modulo 4")
st.image("./src/img/banner.jpg", width=None)

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """            
            ## Obiettivi della lezione
            - Consolidare le competenze acquisite nel Modulo 4
            - Integrare l'uso di ChatGPT, cloud e calendario
            - Creare un flusso di lavoro digitale efficiente
            - Verificare la padronanza degli strumenti avanzati

            ## Contenuti

            ### 1. Integrazione Strumenti Digitali

            #### Progetto 1: Gestione Documenti Intelligente
            1. Utilizzo combinato di:
            - ChatGPT per la creazione contenuti
            - Cloud storage per l'archiviazione
            - Calendario per la pianificazione
            2. Workflow pratico:
            - Generazione documenti con AI
            - Organizzazione nel cloud
            - Pianificazione scadenze

            ### 2. Automazione e Produttività

            #### Progetto 2: Organizzazione Settimanale
            1. Pianificazione attività:
            - Uso del calendario per appuntamenti
            - Gestione to-do list
            - Reminder automatici
            - Condivisione agenda

            2. Gestione documentale:
            - Struttura cartelle cloud
            - Backup automatici
            - Sincronizzazione dispositivi
            - Condivisione selettiva

            ### 3. Comunicazione Efficace

            #### Progetto 3: Collaborazione Digitale
            1. Gestione team virtuale:
            - Calendario condiviso
            - Documenti collaborativi
            - Comunicazione strutturata
            - Tracciamento attività

            2. Ottimizzazione processi:
            - Template standardizzati
            - Workflow automatizzati
            - Reporting periodico
            - Feedback loop

            ### 4. Challenge Finale

            #### Simulazione Ambiente di Lavoro
            1. Scenario completo:
            - Gestione progetti
            - Organizzazione meeting
            - Produzione documenti
            - Collaborazione team

            2. Risoluzione problemi:
            - Gestione imprevisti
            - Ottimizzazione tempi
            - Backup e sicurezza
            - Comunicazione efficace

            ## Esercizi Pratici

            1. Progetto Integrato:
            - Crea contenuti con ChatGPT
            - Organizzali nel cloud
            - Pianifica con il calendario
            - Condividi con altri

            2. Automazione Workflow:
            - Imposta backup automatici
            - Crea template ricorrenti
            - Configura notifiche
            - Ottimizza processi

            3. Challenge Finale:
            - Gestisci un progetto completo
            - Utilizza tutti gli strumenti
            - Risolvi problemi pratici
            - Documenta il processo

            ## Verifica Competenze
            - Integri efficacemente gli strumenti?
            - Gestisci workflow complessi?
            - Ottimizzi i processi?
            - Collabori efficacemente?
""")

# Checklist Finale Modulo 4
st.checkbox("Padronanza ChatGPT")
st.checkbox("Gestione cloud efficiente")
st.checkbox("Uso calendario ottimizzato")
st.checkbox("Integrazione strumenti")
st.checkbox("Automazione processi")
st.checkbox("Collaborazione efficace")

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
