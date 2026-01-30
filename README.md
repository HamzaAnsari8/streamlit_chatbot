# 🤖 Streamlit Chatbot using Gemini API & LangChain

An interactive AI chatbot built using **Streamlit**, **Google Gemini API**, and **LangChain**.  
This project demonstrates how to integrate large language models into a web-based chat interface with prompt management and conversational memory.

---

## 🚀 Features

- 💬 Real-time conversational chatbot UI
- 🧠 Powered by Google Gemini (LLM)
- 🔗 LangChain for prompt handling and chain management
- 🌐 Streamlit-based web interface
- 🔐 Secure API key handling using environment variables
- ♻️ Conversation memory support (optional)

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **LLM**: Google Gemini API  
- **Framework**: LangChain  
- **Language**: Python  
- **Environment Management**: `.env` file  

---

## 📁 Project Structure

main.py # Main Streamlit application
├── chatbot.py # LangChain + Gemini logic
├── requirements.txt # Project dependencies
├── .env # Environment variables (API keys)
├── .gitignore # Ignored files for GitHub
└── README.md # Project documentation



---

## 🔑 Prerequisites

- Python 3.9 or above
- Google Gemini API key
- Basic knowledge of Python and LLMs

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/streamlit-gemini-chatbot.git
   cd streamlit_chatbot

2. creating venv
python -m venv venv
source venv/bin/activate      # For Linux / Mac
venv\Scripts\activate         # For Windows

3. installing dependencies
pip install -r requirements.txt

4.storing API key
GOOGLE_API_KEY=your_gemini_api_key_here

5.runs the application
streamlit run main.py
