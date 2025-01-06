import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 2.4", page_icon="💻", layout="wide")

st.write("# Lezione 2.4: Esercitazioni pratiche Modulo 2")
st.image("./src/img/banner.jpg", width=None)
# st.audio("./src/audio/Pec.wav")

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            ## Obiettivi della lezione
            - Consolidare le competenze acquisite nel Modulo 2
            - Mettere in pratica le conoscenze sulla navigazione web
            - Padroneggiare l'uso di email e PEC
            - Verificare la comprensione generale della comunicazione online

            ## Esercitazioni Complete

            ### 1. Navigazione Web Avanzata

            #### Esercizio 1.1: Ricerche Efficaci
            1. Esegui ricerche su diversi argomenti utilizzando:
               - Operatori di ricerca (AND, OR, virgolette)
               - Filtri avanzati
               - Ricerca per immagini
            2. Confronta i risultati ottenuti
            3. Valuta l'affidabilità delle fonti

            #### Esercizio 1.2: Gestione Browser
            1. Configura il browser:
               - Organizza i preferiti in cartelle
               - Gestisci la cronologia
               - Imposta le estensioni di sicurezza
            2. Crea un ambiente di lavoro efficiente

            ### 2. Gestione Email Professionale

            #### Esercizio 2.1: Comunicazione Efficace
            1. Crea una serie di email professionali:
               - Email formale di presentazione
               - Richiesta di informazioni
               - Invio di documentazione con allegati
            2. Utilizza correttamente:
               - CC e CCN
               - Formattazione del testo
               - Firma professionale

            #### Esercizio 2.2: Organizzazione
            1. Implementa un sistema di gestione email:
               - Crea cartelle tematiche
               - Imposta filtri automatici
               - Configura risposte automatiche
            2. Gestisci efficacemente la posta in arrivo

            ### 3. Utilizzo PEC

            #### Esercizio 3.1: Comunicazioni Ufficiali
            1. Simula l'invio di comunicazioni ufficiali:
               - Prepara documenti formali
               - Invia messaggi PEC
               - Gestisci le ricevute
            2. Archivia correttamente le comunicazioni

            #### Esercizio 3.2: Gestione Documentale
            1. Organizza un sistema di archiviazione PEC:
               - Crea cartelle per tipologia
               - Implementa backup delle ricevute
               - Gestisci le scadenze

            ## Progetto Finale del Modulo

            ### Simulazione Completa
            Crea un flusso di lavoro che integri:
            1. Ricerca di informazioni online
            2. Comunicazione via email
            3. Invio documentazione via PEC
            4. Archiviazione e backup

            ### Documentazione
            Prepara una relazione che descriva:
            - Procedure utilizzate
            - Problemi incontrati
            - Soluzioni adottate
            - Best practice identificate

            ## Verifica delle Competenze
            - Sai navigare in modo sicuro ed efficiente?
            - Gestisci professionalmente le email?
            - Utilizzi correttamente la PEC?
            - Mantieni organizzata la documentazione?    
         """)

st.markdown("## Autovalutazione")
st.markdown("#### Completa la seguente checklist:")
st.checkbox("Navigazione web sicura e efficiente")
st.checkbox("Gestione professionale delle email")
st.checkbox("Utilizzo corretto della PEC")
st.checkbox("Organizzazione documenti digitali")
st.checkbox("Backup e sicurezza dei dati")


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
