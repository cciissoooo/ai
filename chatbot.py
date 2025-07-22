from openai import OpenAI
import uuid

# Initialize the OpenAI client
client = OpenAI()

# Store all active chat sessions
chat_sessions = {}

# Define a common system prompt for all conversations
system_prompt = {
    "role": "system",
    "content": "You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns."
}

# Create a new chat session with a unique identifier
def create_chat():
    chat_id = str(uuid.uuid4())  # Create unique session identifier
    chat_sessions[chat_id] = []  # Initialize empty conversation history
    chat_sessions[chat_id].append(system_prompt)  # Add system prompt to conversation history
    return chat_id

def send_message(chat_id, user_message):
  # Verify chat session exists
  if chat_id not in chat_sessions:
      raise ValueError("Chat session not found!")
  # Add user's message to history
  chat_sessions[chat_id].append({"role": "user", "content": user_message})    
  # Get AI response using conversation history
  response = client.chat.completions.create(
      model="gpt-4",
      messages=chat_sessions[chat_id]
  )
  # Extract and clean AI's response
  answer = response.choices[0].message.content.strip()
  # Add AI's response to history
  chat_sessions[chat_id].append({"role": "assistant", "content": answer})
  # Return AI's response
  return answer

# Create the first chat and send messages
chat_id1 = create_chat()
print("Chat 1, First Message:", send_message(chat_id1, "I'm having trouble with my recent order. Can you help me track it?"))
print("Chat 1, Follow-up Message:", send_message(chat_id1, "It was supposed to arrive yesterday but hasn't. What should I do next?"))

# Create the second chat and send messages
chat_id2 = create_chat()
print("Chat 2, First Message:", send_message(chat_id2, "I'm interested in upgrading my membership. What are the benefits?"))
print("Chat 2, Follow-up Message:", send_message(chat_id2, "Could you guide me through the upgrade process?"))
