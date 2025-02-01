from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import AbstractBase


class Category(AbstractBase):
    __tablename__ = 'categories'
    name = Column(String, unique=True, nullable=False)
    card_rel = relationship("Card", back_populates="category_rel")

    def __str__(self):
        return self.name, self.id
    
    def __repr__(self):
        return f"Category('{self.name}', '{self.id}')"