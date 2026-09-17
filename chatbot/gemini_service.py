from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def ask_gemini(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=message
        )

        return response.text

    except Exception as e:
        print("AI ERROR:", e)  # Render Logs me error dikhega
        return "Sorry, I'm unable to respond right now. Please try again later."