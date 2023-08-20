import bcrypt
from functools import wraps

from flask import request, abort

from app.repositories.user import user_repository


def login_required(func):
    """Basic auth"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if not auth or not user_service.check_auth(auth.username, auth.password):
            abort(401)
        return func(*args, **kwargs)
    return decorated_function

class UserService:
    def encrypt_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password: str, encrypted_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), encrypted_password.encode())

    def check_auth(self, login: str, password: str) -> bool:
        """Check auth data with user data"""
        if user := user_repository.get_or_create(login):
            return self.verify_password(password, user.password)
        return False

    def create_user(self):
        data = request.get_json()
        if data.get('login') and data.get('password'):
            encrypted_password = self.encrypt_password(data.get('password'))
            self.check_is_user_created(data.get('login'))
            if user_repository.get_or_create(data.get('login'), encrypted_password):
                return 200


    def check_is_user_created(self, login: str):
        if user_repository.get_or_create(login):
            return abort(400, "Login is already created")
        
    def get_current_user_id(self) -> int | None:
        if user := user_repository.get_or_create(request.authorization.username):
            return user.id
        return None 
        
user_service = UserService()