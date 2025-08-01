from services.chat_service import ChatService

# Initialize the chat service
chat_service = ChatService()

# Simulate a user ID
user_id = "user123"

# Create a new chat session
chat_id = chat_service.create_chat(user_id)
print(f"Chat session created with ID: {chat_id}")

# Simulate sending a message
user_message = "Hello, how are you?"

try:
    ai_response = chat_service.process_message(user_id, chat_id, user_message)
    print(f"AI Response: {ai_response}")
except Exception as e:
    print(f"Error: {e}")
