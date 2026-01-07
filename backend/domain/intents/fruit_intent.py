from enum import Enum

class FruitIntent(str, Enum):
    COUNT_FRUITS = "count_fruits"  
    FRUIT_WITH_MAX_QUANTITY = "fruit_with_max_quantity"
    FRUITS_BELOW_MIN_STOCK = "fruits_below_min_stock"  
    GET_FRUIT_INFO = "get_fruit_info"  
    SUMMARY = "summary"  