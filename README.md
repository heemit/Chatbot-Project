# Chatbot API with Flask

This is a simple chatbot application built using Flask, designed to handle various user intents such as greetings, inquiries about services, location, and contact information. It uses the Natural Language Toolkit (NLTK) for basic text tokenization and intent detection. The chatbot matches user input with predefined intents and responds accordingly. This API supports CORS for client-side integration and serves an HTML frontend for easy interaction.

## Features:
- Tokenizes user input for intent detection.
- Handles common intents like greetings, thank you messages, service inquiries, and more.
- CORS enabled for frontend communication.
- Easily extensible to add more intents and responses.

## Technologies Used:
- **Flask** (Python Web Framework)
- **NLTK** (Natural Language Processing)
- **Flask-CORS** (Cross-Origin Resource Sharing)

## Installation:

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/chatbot-flask.git
    cd chatbot-flask
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:
    ```bash
    python app.py
    ```

4. Open your browser and visit `http://127.0.0.1:5000/` to interact with the chatbot.
