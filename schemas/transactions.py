from typing import Optional
from pydantic import BaseModel
from datetime import date

class TransactionSchema(BaseModel):
    emitter_id: int
    receiver_id: int
    nature: str
    amount: float


class Transaction(TransactionSchema):
    status: bool
    create_at: date
    update_at: date

    class Config():
        orm_mode: bool = True