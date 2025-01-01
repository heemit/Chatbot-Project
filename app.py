from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

app = Flask(__name__)
CORS(app)  # This is to handle CORS issues

# Preprocessing function
def preprocess(sentence):
    tokens = word_tokenize(sentence.lower())
    return tokens

# Define intents and responses
intents = {
    'greeting': ['hello', 'hi', 'hey', 'greetings'],
    'goodbye': ['bye', 'see you', 'goodbye'],
    'thank_you': ['thank you', 'thanks'],
    'about': ['tell me about your company', 'what is your company', 'about'],
    'services': ['what services do you offer', 'services', 'what can you do'],
    'location': ['where are you located', 'location', 'address'],
    'contact': ['how can I contact you', 'contact', 'phone number', 'email']
}

responses = {
    'greeting': 'Hello! How can I help you today?',
    'goodbye': 'Goodbye! Have a great day!',
    'thank_you': 'You’re welcome!',
    'about': 'We are Acmegrade, providing top-notch AI solutions.',
    'services': 'We offer AI solutions, data analytics, machine learning, and more!',
    'location': 'Our headquarters is located in Mumbai, India.',
    'contact': 'You can reach us via email at contact@acmegrade.com or call us at +91-123-456-7890.'
}

# Function to get intent
def get_intent(message):
    message = message.lower()
    for intent, keywords in intents.items():
        if any(phrase in message for phrase in keywords):
            return intent
    return 'unknown'

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data.get('message', '')
    intent = get_intent(message)
    response = responses.get(intent, "I'm sorry, I didn't understand that.")
    return jsonify({'response': response})

# Serve the index.html file
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
