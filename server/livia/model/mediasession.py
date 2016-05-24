from sqlalchemy import *
from livia.model.base import Base

class MediaSession(Base):
    __tablename__ = "media_session"
 
    Id = Column(Integer, primary_key=True)
    Name = Column(String)