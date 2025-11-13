from project.product import Product


class Drink(Product):
    def __init__(self, name: str) -> None:
        super().__init__(name, 10)

