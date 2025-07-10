# main auth logic
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import init_db, get_db
from schemas import UserCreate, UserLogin
from models import User
from utils import hash_password

app = FastAPI()
init_db()

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(400, detail="Email alread exists")
    new_user = User(
        firstname = user.firstname,
        lastname = user.lastname,
        email = user.email,
        password = hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user






