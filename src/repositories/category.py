from sqlalchemy.orm import Session

from src.models.category import Category


class CategoryRepository:
    def __init__(self, category_model : Category, session : Session):
        self.category_model = category_model
        self.session = session

    def get_many(self) -> list[Category]:
        categories = self.session.query(self.category_model).all()
        return categories
    
#-----------------------------------------------
    def get_id_by_name(self, name : str) -> int:
        category = self.session.query(self.category_model).filter(self.category_model.name == name).first()
        if category:
            return category.id
#-----------------------------------------------        
    
    def add(self, name : str) -> Category:
        category = self.category_model(name=name)
        self.session.add(category)
        self.session.commit()
