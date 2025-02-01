import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base import AbstractBase


class Card(AbstractBase):
    __tablename__ = 'cards'
    name = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    description = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category_rel = relationship("Category", back_populates="card_rel")
    test_rel = relationship("Test", back_populates="card_relationship")

    def __str__(self):
        return self.name, self.id
    
    def __repr__(self):
        return f"Card('{self.name}', '{self.id})"
    
