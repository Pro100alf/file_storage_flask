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
                              f"{os.getenv('POSTGRES_HOST')}:5432/{os.getenv('POSTGRES_DB')}"
    # FIXTURE = ['init.sql']


