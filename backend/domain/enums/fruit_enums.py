from enum import Enum

class FruitCategory(str, Enum):
    CITRUS = "citrus"
    TROPICAL = "tropical"
    BERRY = "berry"
    STONE = "stone"
    OTHER = "other"
    FRESH = "fresh"


class Season(str, Enum):
    SUMMER = "summer"
    WINTER = "winter"
    AUTUMN = "autumn"
    SPRING = "spring"
    ALL_YEAR = "all_year"


class Unit(str, Enum):
    KG = "kg"
    UNIT = "unit"
    BOX = "box"


class OriginType(str, Enum):
    NATIONAL = "national"
    IMPORTED = "imported"
