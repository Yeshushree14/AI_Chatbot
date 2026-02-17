# Customer Service Chatbot

A simple rule-based and NLP-powered chatbot for handling basic customer service queries.

## Features

- Rule-based pattern matching for common queries
- Basic NLP with similarity matching for fallback responses
- Clean, responsive web interface
- Handles queries about: hours, shipping, returns, payments, contact info, order status

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and go to: http://localhost:5000

## Usage

Simply type your questions in the chat interface. The bot can help with:
- Business hours
- Shipping information
- Return policies
- Payment methods
- Contact information
- Order tracking

## Architecture

- `chatbot.py`: Core chatbot logic with pattern matching and NLP
- `app.py`: Flask web server
- `templates/index.html`: Web interface
- `static/style.css`: UI styling
- `static/script.js`: Frontend interactions