import datetime
import re
import random

# Define a function to get a greeting based on the time of day
def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Define a function to perform basic arithmetic operations
def perform_arithmetic(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."
    else:
        return "I can only perform basic arithmetic operations like add, subtract, multiply, and divide."

# Define a function to respond to user inputs
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Define patterns and responses
    patterns = [
        (r"my name is (.*)", "Hello {0}! How are you doing today?", "Hi {0}! Nice to meet you. How's your day going?"),
        (r"hi|hey|hello", f"{get_greeting()} How can I assist you today?", "Hey there! What's up?", "Hi! How's it going?"),
        (r"what is your name ?", "I'm a friendly chatbot created by you. You can call me ChatBot. What's your name?"),
        (r"how are you ?", "I'm just a bunch of code, but I'm doing great! How about you?", "I'm here to help you. How are you feeling today?"),
        (r"sorry (.*)", "No worries at all!", "It's all good!", "Don't worry about it!"),
        (r"I am (.*) good|fine|okay|alright", "That's great to hear!", "Awesome! How can I assist you today?", "Glad to hear that. What's on your mind?"),
        (r"(.*) help (.*)", "Sure, I'm here to help! What do you need assistance with?", "Of course! What do you need help with?"),
        (r"quit", "Goodbye! Take care!", "It was nice chatting with you. See you soon!", "Bye! Have a great day!"),
        (r"(.*) weather in (.*)", "Sorry, I cannot fetch weather information as I don't have internet access."),
        (r"(.*) (created|made) (.*)", "I was created by a clever developer using Python. Do you like programming?"),
        (r"(.*) (favorite|like) (.*)", "I don't have preferences, but I think everything is interesting in its own way!", "I can't say I have a favorite, but I'm here to learn from you!"),
        (r"tell me a joke", "Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"),
        (r"(.*) (add|subtract|multiply|divide) (.*) and (.*)", lambda m: f"The result is {perform_arithmetic(m.group(2), float(m.group(3)), float(m.group(4)))}"),
    ]

    # Check each pattern to see if it matches the user input
    for pattern, *responses in patterns:
        match = re.match(pattern, user_input)
        if match:
            if callable(responses[0]):
                return responses[0](match)
            return random.choice(responses).format(*match.groups())

    return "I'm not sure I understand. Can you rephrase that?"

# Main chatbot function
def chatbot():
    print("Hi! I am your friendly chatbot. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chatbot()
