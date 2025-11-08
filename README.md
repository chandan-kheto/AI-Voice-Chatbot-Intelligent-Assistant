 🤖 AI Voice Chatbot — Intelligent Conversational Assistant

🚀 **An advanced AI chatbot** powered by **Meta LLaMA-3 via OpenRouter API**, built using **Streamlit** with **voice input/output**, smart conversation memory, and real-time speech responses.

> 💬 Talk or type to your personal AI assistant — it listens, remembers context, and speaks back naturally!

---

## 🧠 Features

✅ **Natural Voice Input** — Speak your question directly  
✅ **AI Voice Output (TTS)** — The AI responds with human-like speech  
✅ **Smart Chat Memory** — Remembers past 10 interactions for smooth context  
✅ **Clear Memory Button** — Reset conversation anytime  
✅ **Online Cloud Model** — Powered by OpenRouter (LLaMA-3 Instruct)  
✅ **Streamlit UI** — Clean, modern, and interactive interface  
✅ **Lightweight** — Runs smoothly on CPU, no GPU required  

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| 🧩 Frontend | Streamlit |
| ⚙️ Backend | Python + Requests |
| 🧠 LLM | Meta LLaMA-3 (via OpenRouter API) |
| 🎤 Voice Input | SpeechRecognition |
| 🔊 Voice Output | pyttsx3 |
| 🔐 Secrets | dotenv (.env file for API key) |

---

## 📦 Installation

2️⃣ Create Virtual Environment

python -m venv mvenv
mvenv\Scripts\activate   # (Windows)
3️⃣ Install Dependencies

pip install -r requirements.txt
🔑 Environment Setup
Create a .env file inside your backend folder with your OpenRouter API key:

OPENROUTER_API_KEY=your_openrouter_api_key_here
You can get your free API key here 👉 https://openrouter.ai

🚀 Run the Application

streamlit run app.py
Once it runs, open your browser at:

🌐 http://localhost:8501

🧠 Example Commands
“What is Artificial Intelligence?”

“Who invented deep learning?”

“Summarize the concept of neural networks.”

“Tell me about LLaMA-3.”

“Explain AI ethics.”

🗣️ Voice Controls
🎙️ Speak Now — start voice recording
🔇 Stop Voice — stop speech output instantly
🧹 Clear Memory — reset conversation context

🖼️ Preview
🧠 Voice Chat	💬 Memory
	
(Replace with your own screenshots or GIFs)

⚡ Future Improvements
🌍 Add multiple model switch (Mistral / Phi / Gemma)

🗣️ Integrate more natural TTS voices

💾 Persistent memory (database-backed)

💻 Deploy on Streamlit Cloud

🧑‍💻 Developed by
👨‍💻 Chandan Kheto

💼 Passionate about building intelligent, real-time AI applications.
