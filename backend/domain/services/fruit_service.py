from infra.repositories.fruit_repository import FruitRepository

class FruitService:

    def __init__(self, repository: FruitRepository):
        self.repository = repository
    
    def count_fruits(self) -> int:
        """Retorna o número total de frutas cadastradas"""
        return self.repository.count_fruits()