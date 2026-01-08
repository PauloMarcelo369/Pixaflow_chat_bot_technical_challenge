from domain.intents.fruit_intent import FruitIntent
from domain.services.fruit_service import FruitService

class FruitIntentHandler:
    def __init__(self, service: FruitService): 
        self.service = service
    def handle(self, intent: FruitIntent, params: dict) -> str: 
        if intent == FruitIntent.COUNT_FRUITS.value: 
            return str(self.service.count_fruits()) 
        if intent == FruitIntent.FRUIT_WITH_MAX_QUANTITY.value: 
            return self.service.get_fruit_with_max_quantity() 
        if intent == FruitIntent.FRUITS_BELOW_MIN_STOCK.value: 
            return self.service.get_fruits_below_min_stock() 
        if intent == FruitIntent.GET_FRUIT_INFO.value: 
            return self.service.get_fruit_info(params.get("name")) 
        raise ValueError("Intent não suportada")