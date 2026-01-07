from infra.repositories.fruit_repository import FruitRepository

class FruitService:

    def __init__(self, repository: FruitRepository):
        self.repository = repository
    
    def count_fruits(self) -> int:
        """Retorna o número total de frutas cadastradas"""
        return self.repository.count_fruits()
    
    def get_fruit_with_max_quantity(self) -> str:
        """Retorna a fruta com maior quantidade em formato legível"""
        fruit = self.repository.fruit_with_max_quantity()
        if not fruit:
            return "Nenhuma fruta encontrada."
        return f"{fruit.name} tem a maior quantidade ({fruit.quantity} {fruit.unit})"