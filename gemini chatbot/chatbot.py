import google.generativeai as genai

genai.configure(api_key="GOOGLE_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(history=[])

def chat_with_gemini():
    print("🤖 Gemini ChatBot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye 👋")
            break

        try:
            response = chat.send_message(user_input)
            print("Bot:", response.text)
        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    chat_with_gemini()