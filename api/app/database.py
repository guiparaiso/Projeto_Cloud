from sqlalchemy import event
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import psycopg2
from dotenv import load_dotenv
import os
# URL de conexão do banco de dados

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Criação do engine com a URL de conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"options": "-c timezone=utc"})

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
