import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "meta-llama/llama-3-8b-instruct"

def ask_model(prompt: str, history=None) -> str:
    """Ask OpenRouter API with contextual memory."""
    if not OPENROUTER_API_KEY:
        return "⚠️ Missing API key. Add OPENROUTER_API_KEY to your .env file."

    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/chandan-ai-bot",
            "X-Title": "AI Voice Chatbot",
        }

        # Keep last 10 messages (to save API tokens)
        limited_history = (history or [])[-10:]

        messages = [{"role": "system", "content": "You are a friendly and helpful AI assistant that remembers context."}]
        messages.extend(limited_history)
        messages.append({"role": "user", "content": prompt.strip()})

        payload = {
            "model": MODEL_NAME,
            "messages": messages,
            "max_tokens": 600,
            "temperature": 0.7,
        }

        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        data = response.json()
        if data.get("choices") and data["choices"][0].get("message"):
            return data["choices"][0]["message"]["content"].strip()
        elif data.get("error"):
            return f"⚠️ API Error: {data['error'].get('message', 'Unknown error')}"
        else:
            return f"⚠️ Unexpected response: {data}"

    except requests.exceptions.RequestException as e:
        return f"⚠️ Network Error: {e}"
    except Exception as e:
        return f"⚠️ Unexpected Error: {e}"
