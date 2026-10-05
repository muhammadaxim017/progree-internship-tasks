
def handle_greeting():
    return "Hello! How can I help you?"


def handle_help():
    return "I can help with greetings, general questions, and goodbyes."


def handle_general():
    return "I'm a rule-based chatbot. I respond to messages I recognize."


def handle_name(name):
    return f"Nice to meet you, {name}!" 


def get_response(message):
    message = message.lower().strip(" .,!?")

    if "hello" in message or "hi" in message or "hey" in message:
        if "help" in message:
            return handle_help()
        else:
            return handle_greeting()

    elif "help" in message:
        return handle_help()

    elif "what are you" in message:
        return handle_general()

    else:
        return "Sorry, I don't understand that message."



def main():
    print("Bot: Hello! I'm your chatbot.")
    print("Bot: Type 'bye' or 'exit' to end the conversation.")

    user_name = None

    while True:
        user_message = input("You: ").lower().strip()

        if user_message in ["bye", "exit"]:
            print("Bot: Goodbye! Have a nice day.")
            break

        elif user_message.startswith("my name is "):
            user_name = user_message[len("my name is "):].strip()

            if user_name:
                print("Bot:", handle_name(user_name.title()))
            else:
                print("Bot: Please tell me your name.")
        
        elif user_message == "what is my name":
            if user_name:
                print(f"Bot: Your name is {user_name.title()}.")
            else:
                print("Bot: You haven't told me your name yet.")

        else:
            response = get_response(user_message)
            print("Bot:", response)


if __name__ == "__main__":
    main()