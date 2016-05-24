from sqlalchemy import *
from livia.model.base import Base

class Media(Base):
    __tablename__ = "media"
 
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Code = Column(String)