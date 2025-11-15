
 🤖 AI Voice Chatbot — Intelligent Conversational Assistant

An advanced real-time **AI Voice Assistant** powered by **Meta LLaMA-3 (OpenRouter API)** with a clean **Streamlit UI**, natural **voice input/output**, and smart **conversation memory**.

> 💬 Speak or type to your AI assistant — it listens, understands context, and responds with human-like speech.

---

## 🧠 Features

- 🎙️ **Voice Input** — Speak naturally through your microphone  
- 🔊 **Voice Output (TTS)** — AI responds back using pyttsx3  
- 🧵 **Background Speech Threading** — Smooth non-blocking audio  
- 🧠 **Chat Memory** — Remembers last 10 messages for natural flow  
- 🧹 **Clear Memory** — Reset entire conversation anytime  
- 🌐 **Powered by LLaMA-3** — via OpenRouter cloud API  
- 🖥️ **Streamlit UI** — Clean, interactive, and modern  
- ⚡ **Lightweight** — Works on CPU, no GPU required

---

## 🏗️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | Python + Requests |
| LLM | Meta LLaMA-3 (OpenRouter API) |
| Speech Input | SpeechRecognition |
| Speech Output | pyttsx3 (SAPI5) |
| Environment | python-dotenv (.env) |

---

## 📁 Project Structure

```
Online AI Voice Chatbot/
│
├── app.py             # Streamlit UI + Voice Recognition + TTS + Chat History
├── chat_api.py        # OpenRouter API logic + LLM chat handling + memory
├── .env               # OPENROUTER_API_KEY stored here
├── requirements.txt   # All dependencies
└── README.md          # Project documentation
```

Simple = Clean = No import errors.  
Perfect for beginners, demos, and interviews. ✔

---

## 🧠 Architecture Overview

```
User Voice
    ↓
SpeechRecognition (STT)
    ↓
Text Query
    ↓
OpenRouter LLaMA-3 (LLM)
    ↓
AI Text Response
    ↓
pyttsx3 (TTS Engine)
    ↓
Spoken Voice Output
```

Streamlit handles the UI + buttons + conversation history.

---

## 🧰 Installation

### 1️⃣ Create Virtual Environment
```bash
python -m venv mvenv
mvenv\Scripts\activate    # Windows
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Create a `.env` file inside the project:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Get your API key from 👉 https://openrouter.ai

---

## 🚀 Run the Application

```bash
streamlit run app.py
```

Then open:

🌐 http://localhost:8501

---

## 🗣️ Voice Commands You Can Try

- “What is artificial intelligence?”
- “Explain deep learning in simple words.”
- “Who created LLaMA-3?”
- “Summarize neural networks.”
- “Tell me a fun fact about AI.”

---

## 🎛️ Controls

| Button | Function |
|--------|----------|
| 💬 Send Message | Send typed text |
| 🎙️ Speak Now | Start microphone input |
| 🔇 Stop Voice | Stop the TTS engine |
| 🧹 Clear Memory | Reset chat + API context |

---

## ⚡ Future Improvements

- 🔄 Model switcher (Phi-3, Gemma, Mistral, etc.)  
- 🌍 Multilingual voice support  
- 🧠 Long-term memory (database)  
- 📤 Export chat as PDF/text  
- ☁️ Deploy on Streamlit Cloud  

---

## 👨‍💻 Developer

**Chandan Kheto**  
Passionate about building intelligent, real-time AI applications.

---

## ⭐ Star this repository if you like it!
