from flask import Flask
from controllers.chat_controller import ChatController

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'your_secret_key_here'

# Create an instance of ChatController to handle chat operations
chat_controller = ChatController()

# Define a route for the index page that ensures a user session
@app.route('/')
def index():
    chat_controller.ensure_user_session()
    return "Welcome to the Chatbot Service!"

# Define a route for creating a new chat session
@app.route('/api/create_chat', methods=['POST'])
def create_chat():
    return chat_controller.create_chat()
