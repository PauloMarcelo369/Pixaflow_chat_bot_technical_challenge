from datetime import date
from sqlmodel import select

from infra.db.engine import engine
from domain.models.fruit import Fruit
from domain.enums.fruit_enums import (
    FruitCategory,
    Season,
    Unit,
    OriginType
)
from sqlmodel import Session

def run_seed():
    fruits = [
        Fruit(
            name="Maçã",
            category=FruitCategory.FRESH,
            season=Season.AUTUMN,
            quantity=120,
            unit=Unit.KG,
            min_stock=20,
            origin_type=OriginType.NATIONAL,
            expiration_date=date(2026, 2, 10)
        ),
        Fruit(
            name="Banana",
            category=FruitCategory.FRESH,
            season=Season.ALL_YEAR,
            quantity=200,
            unit=Unit.KG,
            min_stock=30,
            origin_type=OriginType.NATIONAL,
            expiration_date=date(2026, 1, 20)
        ),
        Fruit(
            name="Laranja",
            category=FruitCategory.CITRUS,
            season=Season.WINTER,
            quantity=150,
            unit=Unit.KG,
            min_stock=25,
            origin_type=OriginType.IMPORTED,
            expiration_date=date(2026, 3, 5)
        ),
        Fruit(
            name="Uva",
            category=FruitCategory.FRESH,
            season=Season.SUMMER,
            quantity=90,
            unit=Unit.KG,
            min_stock=15,
            origin_type=OriginType.IMPORTED,
            expiration_date=date(2026, 1, 30)
        ),
        Fruit(
            name="Manga",
            category=FruitCategory.TROPICAL,
            season=Season.SUMMER,
            quantity=60,
            unit=Unit.KG,
            min_stock=10,
            origin_type=OriginType.NATIONAL,
            expiration_date=date(2026, 2, 15)
        ),
    ]

    with Session(engine) as session:
        for fruit in fruits:
            exists = session.exec(
                select(Fruit).where(Fruit.name == fruit.name)
            ).first()

            if not exists:
                session.add(fruit)

        session.commit()


if __name__ == "__main__":
    run_seed()
