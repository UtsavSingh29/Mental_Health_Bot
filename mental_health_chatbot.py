from llama_cpp import Llama
import sys

model_path = "/media/ubuntu/CODE/PlacementProject/MentalWellnessChatbot-master/llama-2-7b-chat.ggmlv3.q2_K.bin"

sys.stderr = open('/dev/null', 'w')  
llm = Llama(model_path=model_path, n_ctx=512)  
sys.stderr = sys.__stderr__

print("Mental Health Chatbot 🤖 - Type 'exit' to quit.")

conversation_history = []

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Take care! If needed, seek professional help. 😊")
        break

    # Store user input in conversation history
    conversation_history.append(f"User: {user_input}")

    # Construct the prompt to keep it **open-ended but still prioritize mental health**  
    formatted_prompt = (
        "You are a mental health chatbot that primarily focuses on mental well-being. However, "
        "you are also allowed to answer general queries when appropriate related to emotions feeling and mental and kind like that. Keep responses supportive and friendly.\n"
        + "\n".join(conversation_history[-5:])  # Keep only the last 5 messages
        + "\nAI (Mental Health Expert):"
    )

    sys.stderr = open('/dev/null', 'w')  
    response = llm(formatted_prompt, max_tokens=100, top_k=50, top_p=0.9)
    sys.stderr = sys.__stderr__

    bot_response = response["choices"][0]["text"].strip()
    bot_response = bot_response.split("User:")[0].strip()  # Avoid repeating user messages

    conversation_history.append(f"AI (Mental Health Expert): {bot_response}")

    print("Bot:", bot_response)
