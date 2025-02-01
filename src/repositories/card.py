from sqlalchemy.orm import Session
from supermemo2 import first_review, review

from src.models.card import Card


class CardRepository:
    def __init__(self, card_model : Card, session : Session):
        self.card_model = card_model
        self.session = session

    def get(self, id : int) -> Card:
        card = self.session.query(self.card_model).filter(self.card_model.id == id).first()
        if card is None:
            raise ValueError(f"Card with id {id} does not exist")
        return card

    def add(self, name : str, description : str, category_id : int) -> None:
        card = self.card_model(name=name, description=description, category_id=category_id)
        self.session.flush(card)
        self.session.add(card)
        self.session.commit()
        return card