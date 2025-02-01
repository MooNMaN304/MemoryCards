import datetime

from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base import AbstractBase


class Test(AbstractBase):
    __tablename__ = 'test'
    grade = Column(Integer, unique=False, nullable=False)
    date_of_creation = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    easiness = Column(Float, default=2.5)
    review_date = Column(DateTime, default=datetime.datetime.utcnow)
    repetition = Column(Integer, default=0)
    interval = Column(Integer, default=1)
    card_id = Column(Integer, ForeignKey('cards.id'), nullable=False)
    card_relationship = relationship("Card", back_populates="test_rel")

    def __str__(self):
        return f"Test {self.grade} on {self.date_of_passing}"
    
    def __repr__(self):
        return f"Test('{self.grade}', '{self.date_of_passing}')"