from supermemo2 import first_review, review

from src.models.test import Test

from datetime import datetime

from src.repositories.card import CardRepository
from src.repositories.test import TestRepository
from src.repositories.category import CategoryRepository

class CardService:
    def __init__(self, card_repository : CardRepository, test_repository: TestRepository, category_repository: CategoryRepository):
        self.card_repository = card_repository
        self.test_repository = test_repository
        self.category_repository = category_repository 

    def create_card(self, name, description, category_id):
        # To DO
        card = self.card_repository.add(name=name, 
                                        description=description, 
                                        category_id=category_id)
        # first_review prints { "easiness": 2.36, "interval": 1, "repetitions": 1, "review_datetime": "2024-06-23 01:06:02"))
        grade = 1 ##
        initial = first_review(grade)
        self.test_repository.add(
           card_id=card.id,
           easiness=initial['easiness'],
           interval=initial['interval'],
           repetition=initial['repetitions'],
           review_date=initial['review_datetime']
       )
        return card

    def get(self, id : int) -> str:
        card_id = self.card_repository.get(id)
        return f'{card_id}'
    
    def _get_cards_due_for_review(self) -> list[Test]:
        card_for_review = []
        for test in self.test_repository.get_many():
            if test.review_date <= datetime.now() and test.grade == 0:
                card_for_review.append(test)
        return card_for_review
    
    def get_count_cards_to_test(self) -> int:
        return len(self._get_cards_due_for_review())
    
    def get_cards_due_for_review(self, category_name: str) -> list[Test]:
        all_unreviewed_cards = self._get_cards_due_for_review()
        cards_due_for_review = []
        for test in all_unreviewed_cards:
            if test.card_relationship.category_rel.name == category_name:
                cards_due_for_review.append(test)
        return cards_due_for_review
        #card.category_id  # преобразовать в f-строки


