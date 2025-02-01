from datetime import datetime
from src.repositories.category import CategoryRepository

class CategoryService:
    def __init__(self, category_repository : CategoryRepository):
        self.category_repository = category_repository

    def get_categories_names(self) -> list[str]:
        categories = self.category_repository.get_many()
        output = []
        for category in categories:
            output.append(category.name)
        return output 
    
    def get_categories_filter_by_card_review(self) -> list[str]:
        categories = self.category_repository.get_many()
        filter_categories = []
        for category in categories:
            for card in category.card_rel:
                for test in card.test_rel:
                    if test.review_date <= datetime.now() and test.grade == 0:
                       filter_categories.append(category.name)
                       break
        return filter_categories
        
    
    
    def get_cards_by_category(self, category_name: str) -> list[str]:
        self.category_repository.get(category_name)