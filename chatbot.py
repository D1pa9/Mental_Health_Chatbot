import nltk
from nltk.tokenize import word_tokenize
import random

# Sample responses for simplicity. This can be replaced with a more sophisticated NLP model.
responses = {
    "greetings": ["Hello!", "Hi there!", "How can I help you today?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "feeling_sad": ["I'm sorry to hear that. It's okay to feel sad sometimes.", "I'm here for you. Tell me more about it."],

    "feeling_happy": ["That's great to hear!", "Awesome! What's making you feel happy?"],
     "seek_professional_help": ["Try to do something that makes you happy.Like exercise,reading."],
}

def get_response(user_message):
    tokens = word_tokenize(user_message.lower())
    
    if any(token in tokens for token in ["hello", "hi", "hey"]):
        return random.choice(responses["greetings"])
    if any(token in tokens for token in ["bye", "goodbye", "see you later"]):
        return random.choice(responses["goodbye"])
    elif any(token in tokens for token in ["sad", "down", "unhappy", "depressed"]):
        return random.choice(responses["feeling_sad"])
    elif any(token in tokens for token in ["clinic", "professional", "suggestions", "tips"]):
        return random.choice(responses["seek_professional_help"])
    elif any(token in tokens for token in ["happy", "joyful", "excited", "great"]):
        return random.choice(responses["feeling_happy"])
    else:
        return 'I am still in process '
  
