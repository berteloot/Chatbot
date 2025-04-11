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
    print("Home route accessed")
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    print("Chat endpoint accessed")
    try:
        data = request.get_json()
        print("Received data:", data)
        user_message = data.get('message', '').lower()
        print("User message:", user_message)
        
        # Simple response logic
        response = responses.get(user_message, responses['default'])
        print("Sending response:", response)
        
        return jsonify({'response': response})
    except Exception as e:
        print("Error in chat endpoint:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True) 