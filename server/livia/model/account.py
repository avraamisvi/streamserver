from sqlalchemy import *
from livia.model.base import Base

class Account(Base):
    __tablename__ = "account"
 
    Id = Column(Integer, primary_key=True)
    Email = Column(String)
    Password = Column(String)