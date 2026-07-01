# Basic Chatbot
# CodeAlpha Internship Task 4

print("=" * 40)
print("          BASIC CHATBOT")
print("=" * 40)
print("Type 'bye' to exit.\n")

while True:

    # Take user input
    user_input = input("You: ").lower()

    # Greetings
    if user_input in ["hello", "hi"]:
        print("Bot: Hi! How can I help you?")

    # Ask about health
    elif user_input == "how are you?":
        print("Bot: I am fine, thanks!")

    # Ask chatbot name
    elif user_input == "what is your name?":
        print("Bot: I am a basic chatbot.")

    # Thank you response
    elif user_input == "thank you":
        print("Bot: You're welcome!")

    # Exit chatbot
    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand.")