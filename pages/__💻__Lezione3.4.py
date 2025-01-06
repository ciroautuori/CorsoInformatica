import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Lezione 3.4", page_icon="💻", layout="wide")

st.write("# Lezione 3.3: Gestione PDF: visualizzazione e modifiche semplici")
st.image("./src/img/banner.jpg", width=None)

# Create three columns
middle_col, right_col = st.columns([2, 1])


# Middle column content
with middle_col:
    st.markdown(
        """
            # Lezione 3.4: Esercitazioni pratiche Modulo 3

## Obiettivi della lezione
- Consolidare le competenze acquisite con Word, Excel e PDF
- Integrare l'uso dei diversi strumenti
- Creare documenti professionali completi
- Risolvere problemi pratici comuni

## Contenuti

### 1. Esercitazioni Microsoft Word

#### Progetto Documento Professionale
1. Creazione lettera commerciale:
   - Intestazione aziendale
   - Formattazione professionale
   - Inserimento logo
   - Piè di pagina con contatti

2. Creazione CV moderno:
   - Layout professionale
   - Sezioni ben organizzate
   - Elementi grafici
   - Esportazione in PDF

### 2. Esercitazioni Microsoft Excel

#### Gestione Contabilità Base
1. Registro spese annuale:
   - Categorie di spesa
   - Calcoli automatici
   - Grafici riepilogativi
   - Formattazione condizionale

2. Budget familiare:
   - Entrate e uscite
   - Previsioni mensili
   - Analisi degli scostamenti
   - Report automatici

### 3. Esercitazioni PDF

#### Gestione Documentale
1. Organizzazione documenti:
   - Unione più documenti
   - Estrazione pagine
   - Aggiunta annotazioni
   - Archiviazione strutturata

2. Conversione e modifica:
   - Da Word a PDF e viceversa
   - Modifica PDF esistenti
   - Protezione documenti
   - Condivisione sicura

### 4. Progetto Integrato

#### Creazione Portfolio Personale
1. Preparazione documenti:
   - CV in Word
   - Analisi competenze in Excel
   - Conversione in PDF
   - Presentazione finale

2. Gestione documentale:
   - Organizzazione file
   - Backup documenti
   - Versioning
   - Condivisione

## Esercizi Pratici Finali

1. Progetto Completo:
   - Crea una presentazione aziendale
   - Includi dati da Excel
   - Converti in PDF professionale
   - Prepara per la condivisione

2. Simulazione Lavoro:
   - Gestisci corrispondenza
   - Organizza dati contabili
   - Prepara reportistica
   - Archivia documenti

3. Challenge Finale:
   - Risolvi problemi comuni
   - Ottimizza i processi
   - Migliora la produttività
   - Automatizza operazioni ripetitive

## Verifica Competenze
- Sai integrare i diversi strumenti?
- Produci documenti professionali?
- Gestisci efficacemente i dati?
- Risolvi problemi in autonomia?
                        
        """)

# Checklist Finale Modulo 3
st.checkbox("Padronanza Word")
st.checkbox("Competenza Excel")
st.checkbox("Gestione PDF")
st.checkbox("Integrazione strumenti")
st.checkbox("Risoluzione problemi")
st.checkbox("Organizzazione efficiente")

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
