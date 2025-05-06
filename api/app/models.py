from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "usuarios" 

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
