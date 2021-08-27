from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from db.base_class import Base


class Transaction(Base):
    id = Column(Integer, primary_key=True, index=True)
    emitter_id = Column(Integer, ForeignKey('user.id'))
    receiver_id = Column(Integer, ForeignKey('user.id'))
    nature = Column(String(30), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Boolean, default=True)
    create_at = Column(Date)
    update_at = Column(Date)
    owner = relationship('User', back_populates='transactions')