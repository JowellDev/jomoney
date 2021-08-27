from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    contact: str
    email: EmailStr

class UserCreate(UserSchema):
    password: str

class User(UserSchema):
    uuid: str
    balance: float
    is_active: bool

    class Config():
        orm_mode: bool = True