from infra.repositories.fruit_repository import FruitRepository

class FruitService:

    def __init__(self, repository: FruitRepository):
        self.repository = repository