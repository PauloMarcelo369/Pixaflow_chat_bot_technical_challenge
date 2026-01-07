from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date, datetime


from domain.enums.fruit_enums import (
    FruitCategory,
    Season,
    Unit,
    OriginType
)

class Fruit(SQLModel, table=True):
    __tablename__ = "fruits"

    id: Optional[int] = Field(default=None, primary_key=True)

    name: str

    category: FruitCategory
    season: Season

    quantity: int
    unit: Unit = Unit.KG
    min_stock: int = 0

    origin_type: OriginType

    expiration_date: Optional[date]

    created_at: datetime = Field(default_factory=datetime.now)