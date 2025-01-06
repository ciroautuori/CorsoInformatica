# Piattaforma Corso di Informatica e Competenze Digitali

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Git LFS](https://img.shields.io/badge/Git%20LFS-F64935?style=for-the-badge&logo=git&logoColor=white)](https://git-lfs.com)

Una piattaforma di apprendimento interattiva progettata per insegnare le basi dell'informatica e le competenze digitali. Questa piattaforma combina moduli di apprendimento strutturati con un assistente basato su IA per fornire un'esperienza educativa completa.

## 🌟 Caratteristiche Principali

- **Interfaccia di Apprendimento Interattiva**: Costruita con Streamlit per un'esperienza utente fluida
- **Assistente basato su IA**: Interfaccia di chat integrata per aiuto e guida in tempo reale
- **Curriculum Completo**: Cinque moduli dettagliati che coprono le competenze digitali essenziali
- **Esercizi Pratici**: Opportunità di apprendimento pratico in ogni modulo
- **Supporto Docker**: Distribuzione containerizzata per ambienti consistenti
- **Multi-piattaforma**: Supporta Windows, macOS e Linux

## 📚 Moduli del Corso

1. **Fondamenti del Computer**
   - Componenti base e funzioni
   - Elementi essenziali del sistema operativo
   - Gestione dei file
   - Esercizi pratici

2. **Internet e Comunicazione**
   - Navigazione sicura in internet
   - Configurazione e utilizzo email
   - Certificati digitali (PEC)
   - Pratica guidata

3. **Microsoft Office Base**
   - Creazione documenti Word
   - Nozioni base di Excel
   - Gestione PDF
   - Esercizi applicativi

4. **Strumenti Digitali Avanzati**
   - Introduzione a ChatGPT
   - Soluzioni di archiviazione cloud
   - Gestione calendario digitale
   - Applicazioni pratiche

5. **Sicurezza Digitale**
   - Gestione password
   - Prevenzione frodi online
   - Strategie di backup dei dati
   - Esercizi sulla sicurezza

## 🚀 Avvio Rapido

### Prerequisiti

1. Installare Git LFS:
   - **Windows**:
     1. Scarica e installa [Git LFS](https://git-lfs.com/)
     2. Apri Git Bash ed esegui:
     ```bash
     git lfs install
     ```

   - **macOS**:
     ```bash
     brew install git-lfs
     git lfs install
     ```

   - **Linux (Ubuntu/Debian)**:
     ```bash
     sudo apt-get install git-lfs
     git lfs install
     ```

2. Installare Ollama (Richiesto per l'Assistente IA):
   - **Windows**:
     1. Scarica l'installer più recente per Windows da [Ollama Releases](https://github.com/ollama/ollama/releases)
     2. Esegui l'installer
     3. Apri PowerShell ed esegui:
     ```powershell
     ollama pull mistral
     ```

   - **macOS**:
     ```bash
     curl https://ollama.ai/install.sh | sh
     ollama pull mistral
     ```

   - **Linux**:
     ```bash
     curl https://ollama.ai/install.sh | sh
     ollama pull mistral
     ```

### Installazione Manuale
1. Installa Python 3.11 o superiore:
   - **Windows**: Scarica da [Python.org](https://www.python.org/downloads/)
   - **macOS**: Usa Homebrew `brew install python@3.11`
   - **Linux**: Usa il gestore pacchetti
     ```bash
     sudo apt-get install python3.11  # Ubuntu/Debian
     ```

2. Configura un ambiente virtuale:
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Windows (Prompt dei Comandi)
python -m venv venv
.\venv\Scripts\activate.bat

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Installa le dipendenze:
```bash
# Tutte le piattaforme
pip install -r requirements.txt
```

4. Avvia l'applicazione:
```bash
# Tutte le piattaforme
streamlit run __💻__Indice.py
```

## 🏗️ Struttura del Progetto

```
├── 📦 src/              # File sorgente e risorse
│   ├── 📂 img/          # Risorse immagini
│   ├── 📂 audio/        # File audio per le lezioni
│   └── 📂 resource/     # PDF e altri documenti
├── 📦 requirements.txt  # Dipendenze Python
├── 📱 __💻__Indice.py   # File principale dell'applicazione
└── 📂 pages/            # Pagine del contenuto del corso
```

## ⚙️ Requisiti Tecnici

- Sistema Operativo:
  - Windows 10/11 con WSL2 (per Docker)
  - macOS 10.15 o più recente
  - Linux (Ubuntu 20.04+, Debian 10+, o simili)
- Python 3.11 o superiore
- Ollama (per la funzionalità dell'assistente IA)
- Browser web moderno (Chrome, Firefox, Edge)
- Connessione internet (solo per la configurazione iniziale e il download del modello)
- Minimo 8GB RAM consigliati
- 10GB di spazio libero su disco (per i modelli)

## 🔧 Risoluzione dei Problemi

### Problemi Comuni

1. **Problemi di Download del Modello Ollama**:
   - Controlla la tua connessione internet
   - Prova a eseguire: `ollama pull mistral --insecure`

2. **Conflitti di Porte**:
   - Assicurati che la porta 11434 non sia in uso

Per altri problemi, controlla la sezione [Issues](https://github.com/[your-username]/Corso_Imparando_Informatica/issues).

## 🤝 Come Contribuire

Accogliamo con piacere i contributi! Segui questi passaggi:

1. Fai il fork del repository
2. Crea un branch per la feature (`git checkout -b feature/NuovaFunzionalità`)
3. Committa le tue modifiche (`git commit -m 'Aggiungi qualche NuovaFunzionalità'`)
4. Pusha sul branch (`git push origin feature/NuovaFunzionalità`)
5. Apri una Pull Request

## 📜 Licenza

Questo progetto è rilasciato sotto la Licenza MIT - vedi il file [LICENSE](LICENSE) per i dettagli.

## 📞 Supporto

Per supporto e domande:
- Apri una issue nel repository
- Contatta i maintainer attraverso il tracker delle issue del repository

## 🙏 Ringraziamenti

- Streamlit per l'incredibile framework web
- Ollama per il supporto al modello IA
- Tutti i contributori che aiutano a migliorare questa piattaforma

---
Realizzato con ❤️ per l'educazione 
