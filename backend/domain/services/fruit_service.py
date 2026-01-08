from infra.repositories.fruit_repository import FruitRepository

class FruitService:

    def __init__(self, repository: FruitRepository):
        self.repository = repository
    
    def count_fruits(self) -> int:
        """Retorna o número total de frutas cadastradas"""
        return self.repository.count_fruits()
    
    def get_all(self) -> str:
        fruits = self.repository.get_all()
        if not fruits:
            return "Não há frutas cadastradas."

        lines = []
        for f in fruits:
            line = (
                f"Nome: {f.name}, "
                f"Categoria: {f.category.value}, "
                f"Estação: {f.season.value}, "
                f"Quantidade: {f.quantity} {f.unit.value}, "
                f"Estoque mínimo: {f.min_stock}, "
                f"Origem: {f.origin_type.value}"
            )
            lines.append(line)

        return "\n".join(lines)
    def get_fruit_with_max_quantity(self) -> str:
        """Retorna a fruta com maior quantidade em formato legível"""
        fruit = self.repository.fruit_with_max_quantity()
        if not fruit:
            return "Nenhuma fruta encontrada."
        return f"{fruit.name} tem a maior quantidade ({fruit.quantity} {fruit.unit})"
    
    def get_fruits_below_min_stock(self) -> str:
        """Retorna todas as frutas abaixo do estoque mínimo"""
        fruits = self.repository.fruits_below_min_stock()
        if not fruits:
            return "Nenhuma fruta está abaixo do estoque mínimo."
        return "\n".join(
            f"- {f.name} (quantidade: {f.quantity}, mínimo: {f.min_stock})"
            for f in fruits
        )
    
    def get_fruit_info(self, name: str) -> str:
        """Retorna detalhes de uma fruta específica"""
        fruit = self.repository.get_by_name(name)
        if not fruit:
            return f"Fruta '{name}' não encontrada."
        return (
            f"{fruit.name}: {fruit.quantity} {fruit.unit}, "
            f"estoque mínimo: {fruit.min_stock}, "
            f"categoria: {fruit.category}, "
            f"origem: {fruit.origin_type}"
        )