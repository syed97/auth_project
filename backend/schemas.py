# define schemas for request and response data for parsing and validation
# using this for handling form data
from pydantic import BaseModel, EmailStr

# for signup
class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str

# for login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# for response data sent to frontend
class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config:
        orm_mode = True

# JWT access token
class Token(BaseModel):
    access_token: str
    token_type: str



