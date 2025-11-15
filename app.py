
import streamlit as st
import os, sys, threading
import speech_recognition as sr
import pyttsx3
import pythoncom

# Link backend
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend"))
sys.path.append(backend_path)
from backend import ask_model

# --- Page Setup ---
st.set_page_config(page_title="AI Voice Chatbot (Online Cloud Model)", page_icon="🤖", layout="wide")
st.title("🤖 AI Voice Chatbot (Online Cloud Model)")
st.markdown("💬 Talk or type — with real-time memory and voice output. Powered by **Llama-3 (OpenRouter)** 🌍")

# --- State Variables ---
if "history_display" not in st.session_state:
    st.session_state.history_display = []
if "history_api" not in st.session_state:
    st.session_state.history_api = []
if "engine" not in st.session_state:
    st.session_state.engine = None
if "speaking" not in st.session_state:
    st.session_state.speaking = False

# --- Voice Engine Setup ---
def init_tts():
    pythoncom.CoInitialize()
    engine = pyttsx3.init(driverName="sapi5")
    engine.setProperty("rate", 175)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id if len(voices) > 1 else voices[0].id)
    return engine

def speak_async(text):
    def _speak():
        try:
            st.session_state.speaking = True
            eng = init_tts()
            st.session_state.engine = eng
            eng.say(text)
            eng.runAndWait()
        except Exception as e:
            print("Speech error:", e)
        finally:
            st.session_state.speaking = False
            st.session_state.engine = None
    threading.Thread(target=_speak, daemon=True).start()

def stop_voice():
    try:
        if st.session_state.speaking and st.session_state.engine:
            st.session_state.engine.stop()
            st.session_state.speaking = False
    except Exception as e:
        print("Stop error:", e)

# --- UI Input ---
user_query = st.text_input("💭 Ask your question:")
col1, col2, col3, col4 = st.columns([1,1,1,1])

# --- Send Button ---
with col1:
    if st.button("💬 Send Message"):
        if user_query.strip():
            with st.spinner("🤖 Thinking..."):
                response = ask_model(user_query, st.session_state.history_api)
            st.session_state.history_api.append({"role": "user", "content": user_query})
            st.session_state.history_api.append({"role": "assistant", "content": response})
            st.session_state.history_display.append(("🧍 You", user_query))
            st.session_state.history_display.append(("🤖 AI", response))
            speak_async(response)

# --- Voice Button ---
with col2:
    if st.button("🎙️ Speak Now"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("🎧 Listening... Speak now!")
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)
        try:
            query = recognizer.recognize_google(audio)
            st.success(f"✅ You said: **{query}**")
            with st.spinner("🤖 Thinking..."):
                response = ask_model(query, st.session_state.history_api)
            st.session_state.history_api.append({"role": "user", "content": query})
            st.session_state.history_api.append({"role": "assistant", "content": response})
            st.session_state.history_display.append(("🧍 You", query))
            st.session_state.history_display.append(("🤖 AI", response))
            speak_async(response)
        except Exception as e:
            st.error(f"⚠️ Voice Input Error: {e}")

# --- Stop Voice ---
with col3:
    if st.button("🔇 Stop Voice"):
        stop_voice()
        st.warning("🛑 Voice stopped.")

# --- Clear Memory Button ---
with col4:
    if st.button("🧹 Clear Memory"):
        st.session_state.history_display.clear()
        st.session_state.history_api.clear()
        st.warning("🧠 Chat memory cleared!")

# --- Display History ---
st.markdown("---")
st.subheader("🗨️ Conversation History")
for role, text in reversed(st.session_state.history_display[-10:]):
    st.markdown(f"**{role}:** {text}")

st.markdown("---")
st.caption("⚡ Powered by Llama-3 • OpenRouter API • Built with ❤️ by Chandan Kheto")

