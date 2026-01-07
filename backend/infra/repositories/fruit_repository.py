from sqlmodel import Session, select
from domain.models.fruit import Fruit
from typing import List, Optional

class FruitRepository:
    def __init__(self, session : Session):
        self.session = session

    def get_all(self) -> List[Fruit]:
        return self.session.exec(select(Fruit)).all()
    
    def count_fruits(self) -> int:
        return self.session.exec(select(Fruit)).count()
    
    def fruit_with_max_quantity(self) -> Optional[Fruit]:
        return self.session.exec(
            select(Fruit).order_by(Fruit.quantity.desc())
        ).first()