from sqlmodel import Session, select
from domain.models.fruit import Fruit
from typing import List, Optional
from sqlalchemy import func

class FruitRepository:
    def __init__(self, session : Session):
        self.session = session

    def get_all(self) -> List[Fruit]:
        return self.session.exec(select(Fruit)).all()
    
    def count_fruits(self) -> int:
       return self.session.exec(select(func.count(Fruit.id))).one()
    
    def fruit_with_max_quantity(self) -> Optional[Fruit]:
        return self.session.exec(
            select(Fruit).order_by(Fruit.quantity.desc())
        ).first()
    
    def fruits_below_min_stock(self) -> List[Fruit]:
        return self.session.exec(
            select(Fruit).where(Fruit.quantity < Fruit.min_stock)
        ).all()
    
    def get_by_name(self, name: str) -> Optional[Fruit]:
        return self.session.exec(
            select(Fruit).where(Fruit.name == name)
        ).first()
    
    def get_by_category(self, category: str) -> List[Fruit]:
        return self.session.exec(
            select(Fruit).where(Fruit.category == category)
        ).all()

    def get_by_season(self, season: str) -> List[Fruit]:
        return self.session.exec(
            select(Fruit).where(Fruit.season == season)
        ).all()
