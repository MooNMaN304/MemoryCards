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


import inquirer
import random

# def main(items:list[str]):
#     questions = [
#     inquirer.List(
#         'first_screen',
#         message=f"Приветствие - у тебя {(CardService.get_count_cards_to_test)} карточек для повторения",
#         choices=["Повторить", "Добавить"],
#             ),
#     ]
#     answers = inquirer.prompt(questions)['first_screen']
#     if answers == "Повторить":
#         question_repeat = [
#         inquirer.List(
#             'repeat',
#             message= f"Просроченность карточки - 13 дней\n",
#             choices= ["Предыдущая", "Оценка", "Следующая"],
#             ),
#         ]
#         return inquirer.prompt(question_repeat)



DATABASE_URL = "sqlite:///example.db"  # SQLite database
engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()


DATABASE_URL = "sqlite:///example.db"  # SQLite database
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# SECOND_SCREEN = {
#     "message" : f"Просроченность карточки - 13 дней\n",
#     "buttons" : ["Предыдущая", "Оценка", "Следующая"],
#     }
# class FirstScreen(Enum):
#     MESSSAGE = 'Просроченность карточки - 13 дней'
#     NEXT_BUTTON = FIRST_SCREEN
    
# class SecondScreen(Enum):
#     MESSSAGE = 'Просроченность карточки - 13 дней'
#     BUTTONS = FirstScreen

# SecondScreen.BUTTONS.MESSAGE

if __name__ == '__main__':
    
    category_repository = CategoryRepository(category_model = Category, session = session)
    card_repository = CardRepository(card_model = Card, session = session)
    test_repository = TestRepository(test_model = Test, session = session)
    category_service = CategoryService(category_repository = category_repository)
    card_service = CardService(card_repository = card_repository, test_repository = test_repository, category_repository = category_repository)
    test_service = TestService(test_repository = test_repository)
    
    # Главный экран с выбором
    # questions = [
    # inquirer.List(
    #     'first_screen',
    #     message=f"Приветствие - у тебя {count_cards} карточек для повторения",
    #     choices=["Повторить", "Добавить"],
    #         ),
    # ]
    # answers = inquirer.prompt(questions)['first_screen']
    
    

    def menu(message: str, choices: list) -> str:
        questions = [
        inquirer.List(
            'screen',
            message= message,
            choices= choices,
                ),
        ]
        answer = inquirer.prompt(questions)
        return answer['screen']
    
    def get_main_menu(first_screen):
        return menu(message=first_screen['message'], choices=first_screen['buttons']) 
    #--------------------------------------

    class MainMenu(Enum):
        TITLE = 'Приветствие - у тебя'
        TITLE2 = "карточек для повторения"
        BUTTONS = ["Повторить", "Добавить"]

    class AddMenu(Enum):
        TITLE = 'Добавить'
        BUTTONS = ["Добавить карточку", "Добавить категорию"]

    class AddCategory(Enum):
        TITLE = 'Добавить категорию'
        MESSAGE = "Введите название категории: "
        SUCESFULL = "Категория добавлена"
        
    class AddCart(Enum):
        TITLE = 'Добавить карточку'
        ANSUCESFULL = 'Нет категорий'
        MESSAGE = 'Выберите категорию'
        NAME = 'Ведите название карточки'
        DESCRIPTION = 'Ведите описание карточки'
        SUCESFULL = 'Карточка успешно создана'

    class RepeatMenu(Enum):
        TITLE = 'Повторить'
        MESSAGE = 'Выберите категорию'
        ANSUCESFULL = 'Нет карточек для повторения в этой категории'
        SUCESFULL = "Поздравляем! Вы прошли все карточки!"

    class RepeatSession(Enum):
        MESSAGE = "Выберите оценку"
        BUTTONS = ["Предыдущая", "Оценка", "Следующая"]
        GRADE = [1, 2, 3, 4, 5]
#--------------------------------------
    
    while True:
        count_cards = card_service.get_count_cards_to_test()
        
        FIRST_SCREEN = {
        "message" : f"{MainMenu.TITLE.value} {count_cards} {MainMenu.TITLE2.value}",
        "buttons" : MainMenu.BUTTONS.value,
        }
    
        user_choice = get_main_menu(FIRST_SCREEN)

        if user_choice == AddMenu.TITLE.value:
            user_add_choice = menu(message=AddMenu.TITLE.value, choices=AddMenu.BUTTONS.value)
            
            if user_add_choice == AddCategory.TITLE.value:
                category_name = input(AddCategory.MESSAGE.value)
                category_repository.add(category_name)
                print(AddCategory.SUCESFULL.value)
            if user_add_choice == AddCart.TITLE.value:
                user_categories = category_service.get_categories_names()
                if len(user_categories) == 0:
                    print(AddCart.ANSUCESFULL.value)
                    continue 
                else:
                    user_category_choice = menu(message=AddCart.MESSAGE.value, choices=user_categories)
                    #print(f'id категории - {category_repository.get_id_by_name(user_category_choice)}')
                    category_id = category_repository.get_id_by_name(user_category_choice)
                    print(AddCart.NAME.value)
                    user_card_name = input()
                    print(AddCart.DESCRIPTION.value)
                    user_card_description = input()
                    card_service.create_card(name=user_card_name, description=user_card_description, category_id=category_id)
                    print(AddCart.SUCESFULL.value)
                    continue

        if user_choice == RepeatMenu.TITLE.value:
            # user_repeat_choice = menu(message='Повторить', choices=[RepeatMenu.BUTTONS.value])
            # if user_repeat_choice == 'Выбрать категорию':
               
            user_categories = category_service.get_categories_filter_by_card_review()

            # отфильтровать категории в которых есть карточки

            user_category_choice = menu(message=RepeatMenu.MESSAGE.value, choices=user_categories)
            cards_for_repeat = card_service.get_cards_due_for_review(user_category_choice)
            if len(cards_for_repeat) == 0:
                print(RepeatMenu.ANSUCESFULL.value)
                continue
            else:
                page = 0
                while True:
                    if len(cards_for_repeat) == 0:
                        print(RepeatMenu.SUCESFULL.value)
                        break
                    try:
                        card = cards_for_repeat[page]
                    except IndexError:
                        continue

                    user_card_repeat = menu(message=f'{card.card_relationship.name}\n{card.card_relationship.description}',
                                                choices=RepeatSession.BUTTONS.value)
                    if user_card_repeat == RepeatSession.BUTTONS.value[0]:
                        page -= 1 if page != 0 else 0
                    elif user_card_repeat == RepeatSession.BUTTONS.value[1]:
                        user_rate = menu(message=RepeatSession.MESSAGE.value, choices=RepeatSession.GRADE.value)
                        test_service.create_new(card, user_rate)
                        del cards_for_repeat[page]
                        continue
                    elif user_card_repeat == RepeatSession.BUTTONS.value[2]:
                        if page < len(cards_for_repeat) - 1:                            
                            page += 1
                           
                        elif page > len(cards_for_repeat) - 1:
                            page = 0
                            
                        else:
                            continue
            
