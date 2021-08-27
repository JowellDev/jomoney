from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.users import User, UserSchema, UserCreate

router = APIRouter()

@router.get('/', response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    return {"message": "get users"}


@router.get('/{user_id}', response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return {"message": "show user"}

@router.post('/register')
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return {"message": "create user"}