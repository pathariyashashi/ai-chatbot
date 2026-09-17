from django.shortcuts import render
from django.http import JsonResponse
from .gemini_service import ask_gemini
import json


# Home Page
def home(request):
    return render(request, "chatbot/index.html")


# Chat API
def chat(request):
    if request.method == "POST":
        try:
            # Frontend se JSON data lena
            data = json.loads(request.body)
            message = data.get("message", "").strip()

            # Empty message check
            if not message:
                return JsonResponse({
                    "reply": "Please type a message first."
                }, status=400)

            # AI Response
            reply = ask_gemini(message)

            # User ko internal errors kabhi mat dikhana
            if (
                "Gemini Error" in reply
                or "503" in reply
                or "404" in reply
                or "UNAVAILABLE" in reply
            ):
                reply = "⚠️ Sorry, I'm a little busy right now. Please try again in a few moments."

            return JsonResponse({
                "reply": reply
            })

        except Exception:
            # Generic error message
            return JsonResponse({
                "reply": "⚠️ Sorry, something went wrong. Please try again."
            }, status=500)

    return JsonResponse({
        "reply": "Invalid Request"
    }, status=400)