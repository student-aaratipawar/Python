import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer (only once)
nltk.download('punkt')

# Define responses
responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! How are you?",
    "hey": "Hey! What can I do for you?",
    "how are you": "I'm just a chatbot, but I'm doing fine!",
    "what is your name": "I'm a simple chatbot created using NLTK.",
    "bye": "Goodbye! Have a nice day!",
    "exit": "Goodbye! Have a nice day!",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
}

def preprocess(sentence):
    tokens = word_tokenize(sentence.lower())
    return tokens

def respond(user_input):
    sentence = user_input.lower().strip()

    if not sentence:
        return "Please type something so I can respond."

    # Full sentence match
    if sentence in responses:
        return responses[sentence]

    # Try matching individual words
    tokens = preprocess(sentence)
    for word in tokens:
        if word in responses:
            return responses[word]

    return "Sorry, I don't understand that."

# Chat loop
print("Chatbot: Hello! Ask me anything or type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower().strip() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Have a nice day!")
        break
    reply = respond(user_input)
    print(f"Chatbot: {reply}")
