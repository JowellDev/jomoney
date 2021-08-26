import uuid

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    uuid = uuid.uuid4()
    contact = Column(String(15), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
