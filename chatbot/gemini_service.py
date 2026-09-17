from google import genai
from django.conf import settings
import time

client = genai.Client(api_key=settings.GEMINI_API_KEY)

SYSTEM_PROMPT = """
You are Apun AI Assistant.

Rules:
- Never mention Gemini, Google AI, model names or API.
- Reply like a helpful human assistant.
- Use Hindi + English naturally.
- Give code inside code blocks.
- Be friendly and professional.
"""

def ask_gemini(message):
    for _ in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=f"{SYSTEM_PROMPT}\n\nUser: {message}"
            )

            return response.text

        except Exception:
            time.sleep(2)

    return "Sorry, I'm busy right now. Please try again in a few moments."