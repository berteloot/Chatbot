from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Simple response dictionary for the chatbot
responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm doing great, thanks for asking!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that. Could you try rephrasing?"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    
    # Simple response logic
    response = responses.get(user_message, responses['default'])
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 