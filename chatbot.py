import re
import random
from difflib import SequenceMatcher

class CustomerServiceChatbot:
    def __init__(self):
        self.responses = {
            'greeting': [
                "Hello! How can I help you today?",
                "Hi there! What can I assist you with?",
                "Welcome! How may I help you?"
            ],
            'hours': [
                "Our business hours are Monday-Friday 9AM-6PM, Saturday 10AM-4PM.",
                "We're open Mon-Fri 9AM-6PM and Sat 10AM-4PM. Closed Sundays."
            ],
            'shipping': [
                "Standard shipping takes 3-5 business days. Express shipping is 1-2 days.",
                "We offer free standard shipping on orders over $50. Express shipping available for $9.99."
            ],
            'returns': [
                "You can return items within 30 days of purchase with original receipt.",
                "Returns are accepted within 30 days. Items must be in original condition."
            ],
            'payment': [
                "We accept all major credit cards, PayPal, and Apple Pay.",
                "Payment options include Visa, MasterCard, AmEx, PayPal, and digital wallets."
            ],
            'contact': [
                "You can reach us at support@company.com or call 1-800-HELP-NOW.",
                "Contact us: Email support@company.com or phone 1-800-HELP-NOW"
            ],
            'order_status': [
                "To check your order status, please provide your order number or email.",
                "I can help you track your order. Please share your order number."
            ],
            'default': [
                "I'm not sure about that. Can you rephrase your question?",
                "Let me connect you with a human agent for better assistance.",
                "Could you provide more details about your inquiry?"
            ]
        }
        
        self.patterns = {
            'greeting': [r'\b(hi|hello|hey|good morning|good afternoon)\b'],
            'hours': [r'\b(hours|open|close|time|when)\b'],
            'shipping': [r'\b(ship|delivery|deliver|send|mail)\b'],
            'returns': [r'\b(return|refund|exchange|back)\b'],
            'payment': [r'\b(pay|payment|card|credit|paypal)\b'],
            'contact': [r'\b(contact|phone|email|call|reach)\b'],
            'order_status': [r'\b(order|track|status|where|shipped)\b']
        }

    def similarity(self, a, b):
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()

    def get_intent(self, message):
        message = message.lower()
        best_match = 'default'
        best_score = 0
        
        for intent, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, message, re.IGNORECASE):
                    return intent
        
        # Fallback to similarity matching
        keywords = {
            'greeting': ['hello', 'hi', 'hey'],
            'hours': ['hours', 'open', 'time'],
            'shipping': ['shipping', 'delivery'],
            'returns': ['return', 'refund'],
            'payment': ['payment', 'pay'],
            'contact': ['contact', 'phone'],
            'order_status': ['order', 'track']
        }
        
        for intent, words in keywords.items():
            for word in words:
                score = max([self.similarity(word, msg_word) for msg_word in message.split()])
                if score > 0.7 and score > best_score:
                    best_score = score
                    best_match = intent
        
        return best_match

    def get_response(self, message):
        intent = self.get_intent(message)
        return random.choice(self.responses[intent])