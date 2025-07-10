# utility functions
from passlib.context import CryptContext
from jose import jwt
from datetime import timedelta, datetime
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
JWT_ENCODING_ALGORITHM = os.getenv("JWT_ENCODING_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expire_time_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire_time = datetime.now(datetime.timezone.utc) + expire_time_delta
    to_encode.update({"exp":expire_time})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ENCODING_ALGORITHM)




