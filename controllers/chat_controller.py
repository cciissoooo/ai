import uuid
from services.chat_service import ChatService

class ChatController:
    def __init__(self):
        self.chat_service = ChatService()
        self.test_session = {}

  def ensure_user_session(self):
    """Ensure user has a session ID in the test session."""
    if 'user_id' not in self.test_session:
        self.test_session['user_id'] = str(uuid.uuid4())
    return self.test_session['user_id']

  def create_chat(self):
    """Handle chat creation request."""
    user_id = self.test_session.get('user_id')
    if not user_id:
        return {'error': 'Session expired'}, 401
    
    chat_id = self.chat_service.create_chat(user_id)
    return {
        'chat_id': chat_id,
        'message': 'Chat created successfully'
    }

  def send_message(self, chat_id, user_message):
    """Handle message sending request."""
    user_id = self.test_session.get('user_id')
    if not user_id:
        return {'error': 'Session expired'}, 401
    
    if not chat_id or not user_message:
        return {'error': 'Missing chat_id or message'}, 400
        
    try:
        ai_response = self.chat_service.process_message(user_id, chat_id, user_message)
        return {'message': ai_response}
    except ValueError as e:
        return {'error': str(e)}, 404
    except RuntimeError as e:
        return {'error': str(e)}, 500
