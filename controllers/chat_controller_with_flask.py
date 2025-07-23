import uuid
from flask import session, request
from services.chat_service import ChatService

class ChatController:
    def __init__(self):
        self.chat_service = ChatService()
    
    def ensure_user_session(self):
        """Ensure user has a session ID."""
        if 'user_id' not in session:
            session['user_id'] = str(uuid.uuid4())
        return session['user_id']
    
    def create_chat(self):
        """Handle chat creation request."""
        user_id = session.get('user_id')
        if not user_id:
            return {'error': 'Session expired'}, 401
        
        chat_id = self.chat_service.create_chat(user_id)
        return {
            'chat_id': chat_id,
            'message': 'Chat created successfully'
        }

    def send_message(self):
        """Handle message sending request."""
        # Retrieve the user_id from the session
        user_id = session.get('user_id')
    
        # Check if the session has expired (user_id is not present)
        if not user_id:
            return {'error': 'Session expired'}, 401
        
        # Extract chat_id and user_message from the incoming JSON request
        chat_id = request.json.get('chat_id')
        user_message = request.json.get('message')
        
        # Check if chat_id or user_message is missing
        if not chat_id or not user_message:
            return {'error': 'Missing chat_id or message'}, 400
            
        try:
            # Process the message using the ChatService and get the AI's response
            ai_response = self.chat_service.process_message(user_id, chat_id, user_message)
            # Return the AI's response as a JSON object
            return {'message': ai_response}
        except ValueError as e:
            # Handle specific error scenarios and return appropriate JSON responses
            return {'error': str(e)}, 404
        except RuntimeError as e:
            return {'error': str(e)}, 500

