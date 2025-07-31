print("🤖 Hi! I'm a simple bot. Type 'quit' to exit.")

while True:
    user_input = input("You: ").lower()
    
    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello there! How can I help?")
    elif "how are you" in user_input:
        print("Bot: I'm just a bot, but I'm doing great!")
    elif "name" in user_input:
        print("Bot: You can call me ChatBot!")
    elif "quit" in user_input or "exit" in user_input:
        print("Bot: Goodbye! 👋")
        break
    else:
        print("Bot: Hmm... I don't understand that yet. Try asking about my name, hello, or how I am.")

  # Run with "python chatbot.py"
