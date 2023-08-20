import os

from dotenv import load_dotenv

basedir = os.path.normpath(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
)
load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@" \
                              f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    MINIO_SERVER_PORT=os.getenv('MINIO_SERVER_PORT')
    MINIO_SERVER_HOST=os.getenv('MINIO_SERVER_HOST')
    MINIO_ROOT_USER=os.getenv('MINIO_ROOT_USER')
    MINIO_ROOT_PASSWORD=os.getenv('MINIO_ROOT_PASSWORD')
        


