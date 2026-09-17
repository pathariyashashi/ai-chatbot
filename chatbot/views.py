from django.shortcuts import render
from django.http import JsonResponse
from .gemini_service import ask_gemini
import json

def home(request):
    return render(request, "chatbot/index.html")

def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message = data.get("message", "")

            reply = ask_gemini(message)

            return JsonResponse({
                "reply": reply
            })

        except Exception as e:
            return JsonResponse({
                "reply": f"Error: {str(e)}"
            }, status=500)

    return JsonResponse({
        "reply": "Invalid Request"
    }, status=400)