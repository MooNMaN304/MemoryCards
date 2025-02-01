from enum import Enum

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models.base import Base
from .models.category import Category
from .models.card import Card
from .models.test import Test

from .repositories.category import CategoryRepository
from .services.category import CategoryService
from .services.card import CardService
from .repositories.card import CardRepository
from .services.test import TestService
from .repositories.test import TestRepository


DATABASE_URL = "sqlite:///example.db"  # SQLite database


engine = create_engine(DATABASE_URL, echo=True)

# clear all data in the database
Base.metadata.drop_all(engine)

# create all tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



if __name__ == '__main__':
    
    category_repository = CategoryRepository(category_model = Category, session = session)
    card_repository = CardRepository(card_model = Card, session = session)
    test_repository = TestRepository(test_model = Test, session = session)
    category_service = CategoryService(category_repository = category_repository)
    card_service = CardService(card_repository = card_repository, test_repository = test_repository, category_repository = category_repository)
    test_service = TestService(test_repository = test_repository)
    
    from faker import Faker
    
    fake = Faker()
    # Create 10 random unique categories
    
    random_categories = []
    for _ in range(1):
        word = fake.unique.word()
        random_categories.append(word)
        category_service.category_repository.add(word)
        
    # Create 100 random unique cards for each category
    for category in random_categories:
        for _ in range(1):
            category_id = category_service.category_repository.get_id_by_name(category)
            name = fake.unique.word()
            card_service.create_card(category_id=category_id, 
                                     description=fake.sentence(), 
                                     name=name)
            
    # Change all data in tests table date to previous day use Test model
    
    # from datetime import datetime, timedelta
    # from sqlalchemy import update
    
    # all_tests = test_service.test_repository.get_many()
    # for test in all_tests:
    #     test_date = test.review_date
    #     previous_day = test_date - timedelta(days=5)
    #     # use model to update
    #     test.review_date = previous_day
    #     session.commit()
    
    
    
    