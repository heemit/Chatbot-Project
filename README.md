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

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/chatbot-flask.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd chatbot-flask
    ```

3. **Install the dependencies**:
    ```bash
    pip install flask nltk flask-cors
    ```

## Usage

1. **Run the Flask app**:
    ```bash
    python app.py
    ```

2. **Access the chatbot**:
   - Open your browser and visit http://127.0.0.1:5000/ to interact with the chatbot via the provided HTML frontend.
   - Alternatively, send POST requests to http://127.0.0.1:5000/chat with user input to receive chatbot responses.

## How It Works

1. **User Input**: The user types a message, such as "Hello".

2. **Intent Matching**:
   - The `match_intent` function scans the user's input for keywords or patterns.
   - If a match is found, it returns the corresponding intent (e.g., `'greeting'`).

3. **Response Generation**:
   - The chatbot looks up the intent in the `intents` dictionary.
   - It returns the predefined response (e.g., "Hello! How can I assist you today?").

4. **Unknown Input**:
   - If no match is found, the chatbot defaults to an "unknown" response, such as "I'm sorry, I didn't understand that."

### Example Flow

- **User Input**: "Hello"
- **Intent Detected**: `greeting`
- **Response**: "Hello! How can I assist you today?"
  
## Extending the Chatbot

To add more intents and responses, follow these steps:

### Define New Intents

1. **Open the `app.py` file**.
2. **Locate the `intents` dictionary**.
3. Add new key-value pairs where:
   - The **key** represents the intent name (e.g., `new_intent`).
   - The **value** is the chatbot's response to that intent.

Example:
```python
intents = {
    'greeting': 'Hello! How can I assist you today?',
    'goodbye': 'Goodbye! Have a great day!',
    'thanks': 'You\'re welcome!',
    'new_intent': 'This is a response to the new intent.'
}
```
