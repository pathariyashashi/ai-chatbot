def get_bot_response(message):

    message = message.lower().strip()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Hello! How can I help you?"

    elif "python" in message:

        if any(word in message for word in ["what", "explain", "meaning", "about"]):
            return "Python is a high-level, interpreted programming language known for its simple and readable syntax."

        elif "variable" in message:
            return "A variable in Python is a name used to store a value."

        elif "loop" in message:
            return "Python mainly provides for and while loops to repeat a block of code."

        elif "function" in message:
            return "A function in Python is a reusable block of code defined using the def keyword."

        elif "list" in message:
            return "A list in Python is an ordered and mutable collection of elements."

        elif "tuple" in message:
            return "A tuple is an ordered and immutable collection of elements in Python."

        elif "dictionary" in message or "dict" in message:
            return "A dictionary stores data in key-value pairs."

        else:
            return "Python is a popular programming language used for web development, data analysis, automation and many other applications."

    elif "django" in message:

        if "model" in message:
            return "A Django Model represents data and usually maps to a database table."

        elif "view" in message:
            return "A Django View contains the logic that processes a request and returns a response."

        elif "template" in message:
            return "A Django Template is an HTML file used to display dynamic data to the user."

        elif "url" in message or "urls.py" in message:
            return "Django URLs map a browser request to the appropriate View."

        elif "mvt" in message or "architecture" in message:
            return "Django follows the MVT pattern: Model handles data, View handles application logic, and Template handles the user interface."

        else:
            return "Django is a Python web framework used to build web applications quickly and securely."

    elif "database" in message:
        return "A database is used to store, organize and manage data."

    elif "sql" in message:
        return "SQL is a language used to communicate with and manage relational databases."

    elif "your name" in message or "who are you" in message:
        return "I am a Rule-Based Chatbot."

    elif "help" in message:
        return "You can ask me about Python, Django, SQL, databases, Models, Views, Templates, URLs, or general greetings."

    elif any(word in message for word in ["thank you", "thanks", "thx"]):
        return "You're welcome! "

    elif any(word in message for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a nice day! "

    else:
        return "Sorry, I don't understand that yet."
    