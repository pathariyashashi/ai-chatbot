from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def ask_gemini(message):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=message
        )

        return response.text if response.text else "Sorry, I couldn't generate a response."

    except Exception as e:
        print("AI ERROR:", str(e))
        return "Sorry! I'm unable to respond right now."