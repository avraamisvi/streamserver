from sqlalchemy import *
from livia.model.base import Base

class MediaCategory(Base):
    __tablename__ = "media_category"
 
    Id = Column(Integer, primary_key=True)
    Name = Column(String)