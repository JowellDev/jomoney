from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.transactions import Transaction, TransactionSchema

router = APIRouter()

@router.get('/', response_model=List[Transaction])
def get_all_transactions(db: Session = Depends(get_db)):
    return {"message": "get transaction"}


@router.get('/{transaction_id}', response_model=Transaction)
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return {"message": "show transaction"}