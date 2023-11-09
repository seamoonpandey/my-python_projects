import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!']),
    (r'how are you', ['I am good, thank you. How about you?', 'I am a chatbot, so I am always ready to help.']),
    (r'what is your name', ["I am a chatbot, and you can call me ChatGPT."]),
    (r'who are you', ["I am ChatGPT, a text-based chatbot."]),
    (r'quit', ['Goodbye!', 'Bye!']),
]

chatbot = Chat(patterns, reflections)

print("Hello! Mate I'm you AI friend. I can't show you your dirty desires but I can talk to you alright.")

chatbot.converse()
