from sqlalchemy import *
from livia.model.base import Base

class MediaType(Base):
    __tablename__ = "media_type"
 
    Id = Column(Integer, primary_key=True)
    Name = Column(String)