# Invoice Reimbursement System

An end-to-end application for automating employee invoice reimbursement analysis against company policy, and providing an AI-powered chat assistant for follow-up queries.

---

## 🎬 Demo and Repository

- **📹 Video Demonstration**: [Watch Complete Demo](https://drive.google.com/file/d/1rhoqm8pzHS9wEQELTq1qMyauanaiLI5n/view?usp=sharing)
- **💻 Source Code**: [GitHub Repository](https://github.com/s11saurabh/IAI_solution_Assignment)


<img width="1468" alt="image" src="https://github.com/user-attachments/assets/7e8206f4-fb2e-44b8-a216-cae54a716e24" />
<img width="1460" alt="image" src="https://github.com/user-attachments/assets/6cfbaef8-980b-4a74-9218-0119f87cf869" />
<img width="1434" alt="image" src="https://github.com/user-attachments/assets/70e61c91-52fd-45a7-b6f0-31fb18ed9471" />
<img width="1384" alt="image" src="https://github.com/user-attachments/assets/d10312e5-8e47-48ae-b573-5f055b747539" />
<img width="1464" alt="image" src="https://github.com/user-attachments/assets/0eccd677-79cb-4b88-9992-4764aeac6ad1" />
<img width="1468" alt="image" src="https://github.com/user-attachments/assets/750666ec-1339-4630-9b95-c6f798ca89f6" />



## 🚀 Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Application](#running-the-application)
6. [Project Structure](#project-structure)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [License](#license)

---

## 🔍 Features

* **Invoice Analysis**: Upload company policy (PDF) and a ZIP of invoices for automated analysis.
* **AI Chat Assistant**: Ask follow-up questions about reimbursement decisions and policies.
* **System Health**: Check backend API status at a glance.
* **Vector Store**: Persist analysis results for contextual chat queries.

---

## 🛠️ Tech Stack

| Component        | Technology                                                       | Purpose                                            |
| ---------------- | ---------------------------------------------------------------- | -------------------------------------------------- |
| Backend API      | **[FastAPI](https://fastapi.tiangolo.com/)**                     | High-performance asynchronous web framework.       |
| HTTP Server      | **[Uvicorn](https://www.uvicorn.org/)**                          | ASGI server for running the FastAPI app.           |
| Frontend         | **[Streamlit](https://streamlit.io/)**                           | Rapid UI development for data apps.                |
| LLM Integration  | **[Google Gemini API](https://developers.generativeai.google/)** | Natural language understanding & generation.       |
| Embeddings       | **[sentence-transformers](https://www.sbert.net/)**              | Generate and search semantic embeddings.           |
| Database         | **[MongoDB](https://www.mongodb.com/)**                          | Store analysis results and vector embeddings.      |
| PDF Parsing      | **[PyPDF2](https://pythonhosted.org/PyPDF2/)**                   | Extract text from PDF policy & invoices.           |
| Environment Vars | **[python-dotenv](https://github.com/theskumar/python-dotenv)**  | Manage `.env` configuration.                       |
| Packaging & Venv | `venv`, **pip**                                                  | Python virtual environment and package management. |

---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/invoice-reimbursement-system.git
cd invoice-reimbursement-system

# 2. Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Upgrade core tools
pip install --upgrade pip setuptools wheel

# 4. Install Python dependencies
pip install -r requirements.txt
```

---

## 🔧 Configuration

Create a `.env` file in the project root with the following entries:

```dotenv
# Google Gemini API key
GEMINI_API_KEY=YOUR_GOOGLE_API_KEY

# MongoDB connection URI\DATABASE_URL=mongodb+srv://<user>:<pass>@cluster0.mongodb.net/mydb?retryWrites=true&w=majority
```

Load them automatically when running:

```bash
# Bash / zsh
set -a && source .env && set +a
```

---

## ▶️ Running the Application

### Start the FastAPI backend

```bash
uvicorn main:app --reload --port 8000
```

### Start the Streamlit frontend

```bash
streamlit run streamlit_app.py --server.port 8501
```

Open your browser at [http://localhost:8501](http://localhost:8501) to access the UI.

---

## 🗂️ Project Structure

```
invoice-reimbursement-system/
├── main.py               # FastAPI application entrypoint
├── services/             # Business logic (LLM, vector store)
├── models/               # Pydantic schemas & data models
├── pdf_processor.py      # PDF text extraction utility
├── streamlit_app.py      # Frontend Streamlit application
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API keys, DB URI)
└── README.md             # This documentation
```

---

## 🎯 Usage

1. **Invoice Analysis**: Select the "Invoice Analysis" page, upload your policy PDF and invoice ZIP, then click **Analyze**.
2. **Chat Assistant**: Switch to "Chat Assistant" to ask contextual questions about past analyses (powered by vector search + LLM).
3. **System Health**: Use "System Health" to verify the backend is running correctly.

---

## 🤝 Contributing

Contributions are welcome! Please open issues or pull requests for enhancements, bug fixes, or new features.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
