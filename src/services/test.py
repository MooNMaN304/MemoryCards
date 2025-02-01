from supermemo2 import first_review, review

from src.repositories.test import TestRepository
from src.models.test import Test

class TestService:
    def __init__(self, test_repository : TestRepository,
                 ):
        self.test_repository = test_repository
        # self.card_repository = card_repository
        # self.category_repository = category_repository

    def get(self, id : int) -> str:
        test_id = self.test_repository.get(id)
        return f'{test_id}'
    
    def create_new(self, test: Test, grade: int) -> None:
        # create new value for test
        new_test = review(quality=test.grade,
                          easiness=test.easiness,
                          interval=test.interval, 
                          repetitions=test.repetition,
                          review_datetime=test.review_date)
        
        self.test_repository.update_grade(id=test.card_relationship.id,
                                          grade=grade)
        
        self.test_repository.add(card_id=test.card_relationship.id,
                             easiness=new_test['easiness'],
                               review_date=new_test['review_datetime'],
                               repetition=new_test['repetitions'],
                               interval=new_test['interval'], 
                               )





    