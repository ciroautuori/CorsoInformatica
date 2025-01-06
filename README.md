# Computer Science and Digital Skills Course Platform

[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Git LFS](https://img.shields.io/badge/Git%20LFS-F64935?style=for-the-badge&logo=git&logoColor=white)](https://git-lfs.com)

An interactive learning platform designed to teach fundamental computer science and digital skills. This platform combines structured learning modules with an AI-powered assistant to provide a comprehensive educational experience.

## 🌟 Key Features

- **Interactive Learning Interface**: Built with Streamlit for a seamless user experience
- **AI-Powered Assistant**: Integrated chat interface for real-time help and guidance
- **Comprehensive Curriculum**: Five detailed modules covering essential digital skills
- **Practical Exercises**: Hands-on learning opportunities in each module
- **Docker Support**: Containerized deployment for consistent environments
- **Cross-Platform**: Supports Windows, macOS, and Linux

## 📚 Course Modules

1. **Computer Fundamentals**
   - Basic components and functions
   - Operating system essentials
   - File management
   - Practical exercises

2. **Internet and Communication**
   - Safe internet navigation
   - Email configuration and usage
   - Digital certificates (PEC)
   - Hands-on practice

3. **Basic Microsoft Office**
   - Word document creation
   - Excel spreadsheet basics
   - PDF management
   - Applied exercises

4. **Advanced Digital Tools**
   - ChatGPT introduction
   - Cloud storage solutions
   - Digital calendar management
   - Practical applications

5. **Digital Security**
   - Password management
   - Online fraud prevention
   - Data backup strategies
   - Security exercises

## 🚀 Quick Start

### Prerequisites

1. Install Git LFS:
   - **Windows**:
     1. Download and install [Git LFS](https://git-lfs.com/)
     2. Open Git Bash and run:
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

2. Install Ollama (Required for AI Assistant):
   - **Windows**:
     1. Download the latest Windows installer from [Ollama Releases](https://github.com/ollama/ollama/releases)
     2. Run the installer
     3. Open PowerShell and run:
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

### Manual Installation 
1. Install Python 3.11 or higher:
   - **Windows**: Download from [Python.org](https://www.python.org/downloads/)
   - **macOS**: Use Homebrew `brew install python@3.11`
   - **Linux**: Use your package manager
     ```bash
     sudo apt-get install python3.11  # Ubuntu/Debian
     ```

2. Set up a virtual environment:
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Windows (Command Prompt)
python -m venv venv
.\venv\Scripts\activate.bat

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
# All platforms
pip install -r requirements.txt
```

4. Run the application:
```bash
# All platforms
streamlit run __💻__Indice.py
```

## 🏗️ Project Structure

```
├── 📦 src/              # Source files and assets
│   ├── 📂 img/          # Image assets
│   ├── 📂 audio/        # Audio files for lessons
│   └── 📂 resource/     # PDF and other documents
├── 📦 requirements.txt  # Python dependencies
├── 📱 __💻__Indice.py   # Main application file
└── 📂 pages/            # Course content pages

## ⚙️ Technical Requirements

- Operating System:
  - Windows 10/11 with WSL2 (for Docker)
  - macOS 10.15 or newer
  - Linux (Ubuntu 20.04+, Debian 10+, or similar)
- Python 3.11 or higher
- Docker and Docker Compose
- Ollama (for AI assistant functionality)
- Modern web browser (Chrome, Firefox, Edge)
- Internet connection (only for initial setup and model download)
- Minimum 8GB RAM recommended
- 10GB free disk space (for models)

## 🔧 Troubleshooting

### Common Issues

1. **Ollama Model Download Issues**:
   - Check your internet connection
   - Try running: `ollama pull mistral --insecure`

2. **Port Conflicts**:
   - Ensure ports 8501 and 11434 are not in use
   - Change ports in docker-compose.yml if needed

For more issues, check the [Issues](https://github.com/[your-username]/Corso_Imparando_Informatica/issues) section.

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and queries:
- Open an issue in the repository
- Contact the maintainers through the repository's issue tracker

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- Ollama for the AI model support
- All contributors who help improve this platform

---
Made with ❤️ for education 