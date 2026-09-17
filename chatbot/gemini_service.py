from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def ask_gemini(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=message
        )

        # Safe response
        if hasattr(response, "text") and response.text:
            return response.text

        return "Sorry, I couldn't generate a response."

    except Exception as e:
        # Render logs me actual error print hoga
        print("AI ERROR:", str(e))

        # User ko generic message hi dikhe
        return "Sorry! I'm unable to respond right now."