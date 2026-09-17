from google import genai
from django.conf import settings
import time
import random

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def ask_gemini(message):
    """Gemini AI with automatic retry."""

    for attempt in range(5):   # 5 retries
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=message,
            )

            if response.text:
                return response.text

            return "Sorry, I couldn't generate a response."

        except Exception as e:
            error = str(e)

            # Retry only for temporary server issues
            if "503" in error or "UNAVAILABLE" in error:
                wait = (2 ** attempt) + random.random()
                time.sleep(wait)
                continue

            return f"Gemini Error: {error}"

    return "⚠️ Gemini AI is busy right now. Please try again in a few seconds."