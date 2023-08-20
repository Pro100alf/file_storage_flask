from datetime import datetime

from sqlalchemy import (Column, DateTime, Integer, String)
from sqlalchemy.orm import declarative_base

from . import db


class User(db.Model):
    id = Column(Integer, primary_key=True)
    login = Column(String(255), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    create_ts = Column(DateTime, nullable=False, default=datetime.utcnow)