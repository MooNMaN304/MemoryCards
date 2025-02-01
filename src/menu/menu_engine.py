# # from sqlalchemy import create_engine
# # from sqlalchemy.orm import sessionmaker

# # from .models.base import Base
# # from .models.category import Category
# # from .models.card import Card
# # from .models.test import Test

# # from .repositories.category import CategoryRepository
# # from .services.category import CategoryService
# # from src.services.card import CardService
# # from .repositories.card import CardRepository
# # from .services.test import TestService
# # from .repositories.test import TestRepository

# #------------------------------------------------------------------------------

# import inquirer

# FIRST_SCREEN = {
#     "message" : f"Приветствие - у тебя {CardService.get_count_cards_to_test()} карточек для повторения",
#     "buttons" : ["Повторить", "Добавить"],
#     }

# SECOND_SCREEN = {
#     "message" : f"Просроченность карточки - 13 дней\n",
#     "buttons" : ["Предыдущая", "Оценка", "Следующая"],
#     }

# def menu(message: str, choices: list) -> str:
#     questions = [
#     inquirer.List(
#         message= message,
#         choices= choices,
#             ),
#     ]
#     answer = inquirer.prompt(questions)
#     return answer
#     # if answers == FIRST_SCREEN["buttons"][0]:
#     #     question_repeat = [
#     #     inquirer.List(
#     #         'repeat',
#     #         message= SECOND_SCREEN["message"],
#     #         choices= SECOND_SCREEN["buttons"],
#     #         ),
#     #     ]
#     #     return inquirer.prompt(question_repeat)







# # main(FIRST_SCREEN)
# #------------------------------------------------------------------------------


# # DATABASE_URL = "sqlite:///example.db"  # SQLite database
# # engine = create_engine(DATABASE_URL, echo=True)

# # Session = sessionmaker(bind=engine)
# # session = Session()


# # DATABASE_URL = "sqlite:///example.db"  # SQLite database
# # engine = create_engine(DATABASE_URL, echo=True)
# # Base.metadata.create_all(engine)

# # Session = sessionmaker(bind=engine)
# # session = Session()


# # if __name__ == '__main__':
    
# #     category_repository = CategoryRepository(category_model = Category, session = session)
# #     card_repository = CardRepository(card_model = Card, session = session)
# #     test_repository = TestRepository(test_model = Test, session = session)
# #     category_service = CategoryService(category_repository = category_repository)
# #     card_service = CardService(card_repository = card_repository, test_repository = test_repository)
# #     # Главный экран с выбором
    
# #     # Сделать создание категорий
    
# #     # Сделать меню добавления
    
# #     # Сделать добавление карточки
# #     user_choice = main(category_service.get_categories_names())
# #     list_cards = category_service.get_cards_by_category(user_choice)
    
    
    


















