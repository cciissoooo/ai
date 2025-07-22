from models.chat import ChatManager

def load_system_prompt(file_path: str) -> str:
    """Load the system prompt from file."""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading system prompt: {e}")
        return "You are a helpful assistant."

# Load the system prompt
system_prompt = load_system_prompt('data/system_prompt.txt')

# Initialize manager
manager = ChatManager()

# Create a new chat
user_id = "test_user"
chat_id = "test_chat"
manager.create_chat(user_id, chat_id, system_prompt)

# Add some messages
messages = [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there!"},
    {"role": "user", "content": "How are you?"},
    {"role": "assistant", "content": "I'm just a program, but I'm here to help!"}
]
