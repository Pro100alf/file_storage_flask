import io

from minio import Minio, S3Error
from urllib3.response import HTTPResponse

from app.config import Config

settings = Config()

class MinioService:
    def __init__(self):
        self.client = Minio(
            endpoint=f"{settings.MINIO_SERVER_HOST}:{settings.MINIO_SERVER_PORT}",
            access_key=settings.MINIO_ROOT_USER,
            secret_key=settings.MINIO_ROOT_PASSWORD,
            secure=False,
        )
        self.bucket = 'file-storage'
        self.create_bucket(self.bucket)

    def check_file_exists(self, file_path: str) -> bool:
        try:
            self.client.stat_object(self.bucket, file_path)
            return True
        except S3Error:
            return False

    def put_file(self, file_name: str, bytes_data: bytes, file_length: int, content_type: str) -> HTTPResponse:
        file_dir = file_name[:2]
        return self.client.put_object(
            bucket_name=self.bucket,
            object_name=f"{file_dir}/{file_name}",
            data=bytes_data,
            length=file_length,
            content_type=content_type
        )

    def get_file(self, file_path: str) -> HTTPResponse | None:
        if not self.check_file_exists(file_path=file_path):
            return None
        response = self.client.get_object(
            bucket_name=self.bucket,
            object_name=file_path,
        )

        return response
    
    def delete_file(self, file_path: str) -> HTTPResponse | None:
        if not self.check_file_exists(file_path=file_path):
            return None
        response = self.client.remove_object(
            bucket_name=self.bucket,
            object_name=file_path,
        )
        return response
    
    def create_bucket(self, bucket_name: str):
        if not self.check_bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)

    def check_bucket_exists(self, bucket_name: str) -> bool:
        return self.client.bucket_exists(bucket_name)


minio_service = MinioService()
