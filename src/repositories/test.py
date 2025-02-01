from supermemo2 import first_review, review

import datetime

from sqlalchemy.orm import Session

from src.models.test import Test


class TestRepository:
    def __init__(self, test_model : Test, session : Session):
        self.test_model = test_model
        self.session = session

    def get(self, id : int) -> Test:
        test_instance = self.session.query(self.test_model).filter_by(id=id).first()
        if test_instance is None:
            raise ValueError(f"Test with id {id} not found.")
        return test_instance
    
    def add(self, card_id : int, easiness : float, review_date :datetime ,repetition :int ,interval :int, grade : int = 0,) -> Test:
        # To Do
        new_test = self.test_model(
           card_id=card_id,
           grade=grade,
           easiness=easiness,
           interval=interval,
           repetition=repetition,
           review_date=review_date
       )
        self.session.add(new_test)
        self.session.commit()
        return new_test
    
    def get_many(self) -> list[Test]:
        tests = self.session.query(self.test_model).all()
        return tests
    
    def update_grade(self, id: int, grade: int) -> None:
        test_instance = self.get(id)
        test_instance.grade = grade
        #test_instance.
        # как при вызове метода update_grade() не обновляются данные?
        self.session.commit()
