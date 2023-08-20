from datetime import datetime

from sqlalchemy import (Column, DateTime, Integer, String)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql.schema import ForeignKey

from . import db

class File(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String, nullable=False)
    original_name = Column(String, nullable=False)
    create_ts = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    @hybrid_property
    def directory(self):
        return self.name[:2]