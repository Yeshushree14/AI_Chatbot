from flask import Flask, render_template, request, jsonify
from chatbot import CustomerServiceChatbot

app = Flask(__name__)
bot = CustomerServiceChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message.strip():
        return jsonify({'response': 'Please enter a message.'})
    
    bot_response = bot.get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)