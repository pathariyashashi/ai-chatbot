def get_bot_response(message):

    message = message.lower().strip()


    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "what is django" in message or "django" in message and "what" in message:
        return "Django is a Python web framework used to build web applications quickly and securely."

    elif "how django works" in message or "how does django work" in message:
        return "Django follows the MVT pattern: Model handles data, View handles logic, and Template handles the user interface."

    elif "django model" in message:
        return "A Django Model represents data and usually maps to a database table."

    elif "django view" in message:
        return "A Django View contains the logic that processes a request and returns a response."

    elif "django template" in message:
        return "A Django Template is an HTML file that displays dynamic data to the user."

    elif "django url" in message or "urls.py" in message:
        return "Django URLs map a browser request to the appropriate View function or class."

    elif "your name" in message or "what is your name" in message:
        return "I am a Rule-Based Chatbot."

    elif "help" in message:
        return "You can ask me about Django, Models, Views, Templates, URLs, or greetings."

    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a nice day!"
    
    else:
        return "Sorry, I don't understand that yet."
