from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def ask_gemini(message):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",   # Updated model
            contents=message
        )

        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"