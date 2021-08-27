from uuid import uuid4

from sqlalchemy import Column, String, Integer, Boolean, Float, Date
from sqlalchemy.orm import relationship
from db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(50), default=uuid4())
    contact = Column(String(15), nullable=False)
    email = Column(String(30), nullable=False)
    balance = Column(Float, default=0)
    password = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    create_at = Column(Date)
    transactions = relationship('Transaction', back_populates='owner')