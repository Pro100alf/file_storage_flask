from app.models.user import User
from app.repositories import base
from app.models import db

class UserRepository(base.Base[User]):

    def __init__(self):
        super(UserRepository, self).__init__(User)
        
    def get_or_create(self, login: str, password: str = None) -> User:
        if not password:
            if user := self._get_where(login=login):
                return user
        else:
            user = User(login=login, password=password)
            db.session.add(user)
            db.session.commit()
            return user
        
user_repository = UserRepository()
            