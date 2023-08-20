import hashlib

from flask import request, abort

from app.repositories.file import file_repository
from app.services.user import user_service
from app.services.minio import minio_service

class FileService:
    def checksum_md5(self, file: bytes, block_size=2**20) -> str:
        md5 = hashlib.md5()
        while True:
            data = file.read(block_size)
            if not data:
                break
            md5.update(data)
        return md5.hexdigest()

    def upload_file(self):
        if 'file' in request.files:
            file = request.files['file']
            md5_sum = self.checksum_md5(file)
            if user_id := user_service.get_current_user_id():
                try:
                    minio_service.put_file(md5_sum, file, file.content_length, file.content_type)
                except Exception:
                    abort(400, "Can't save file")
                if file_repository.create(user_id, md5_sum, file.filename):
                    return {"file_hash": md5_sum}
        return abort(500)
        
file_service = FileService()
            