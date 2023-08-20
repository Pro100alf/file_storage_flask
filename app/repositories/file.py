from app.models.file import File
from app.repositories import base
from app.models import db

class FileRepository(base.Base[File]):

    def __init__(self):
        super(FileRepository, self).__init__(File)
        
    def get(self, name: str) -> File:
        if file := self._get_where(name=name):
            return file
        
    def create(self, user_id: int, name: str, original_name: str) -> File:
        file = File(user_id=user_id,
                    name=name,
                    original_name=original_name)
        db.session.add(file)
        db.session.commit()
        return file
        
file_repository = FileRepository()
            