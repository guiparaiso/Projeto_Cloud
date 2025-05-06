from fastapi import FastAPI, HTTPException, Depends,Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from jose import JWTError, jwt
from jose import jwt, JWTError  # Certifique-se de importar JWTError
import yfinance as yf
from pydantic import BaseModel
from database import get_db
from dotenv import load_dotenv
import os
import models
import bcrypt
from models import Base
from database import engine  # seu engine SQLAlchemy
import pandas as pd
import requests

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")


Base.metadata.create_all(bind=engine)

# Database setup

# Create database engine
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Database dependency

# Models
class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str

class UserLogin(BaseModel):
    email: str
    senha: str

class Token(BaseModel):
    jwt: str


# Funções de autenticação
def create_access_token(data: dict):
    to_encode = data.copy()
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return email
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:  # Altere de PyJWTError para JWTError
        raise HTTPException(status_code=401, detail="Invalid token")


# Endpoints
@app.post("/registrar", response_model=Token)
def registrar(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    hashed = bcrypt.hashpw(user.senha.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(
        email=user.email,
        nome=user.nome,
        senha=hashed.decode('utf-8')  # armazena como string

    )
    db.add(db_user)
    db.commit()

    token = create_access_token({"sub": user.email})
    return {"jwt": token}

@app.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not bcrypt.checkpw(user.senha.encode('utf-8'), db_user.senha.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"jwt": token}



ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

@app.get("/consultar")
def cotacao_euro(current_user: str = Depends(verify_token)):
    try:
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": "EUR",
            "to_currency": "USD",
            "apikey": ALPHA_VANTAGE_API_KEY
        }

        response = requests.get(url, params=params)
        data = response.json()

        if "Realtime Currency Exchange Rate" not in data:
            raise HTTPException(status_code=500, detail="No exchange data found")

        exchange_info = data["Realtime Currency Exchange Rate"]
        result = {
            "from_currency": exchange_info["1. From_Currency Code"],
            "to_currency": exchange_info["3. To_Currency Code"],
            "rate": exchange_info["5. Exchange Rate"],
            "last_updated": exchange_info["6. Last Refreshed"]
        }

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch exchange rate: {e}")
