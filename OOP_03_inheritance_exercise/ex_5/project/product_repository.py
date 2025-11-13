from typing import Optional

from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        product = [p for p in self.products if p.name == product_name][0]
        return product

    def remove(self, product_name: str) -> Product | None:
        try:
            product = [p for p in self.products if p.name == product_name][0]
            self.products.remove(product)
        except IndexError:
            pass

    def __repr__(self) -> str:
        result = ""
        for p in self.products:
            result += f"{p.name}: {p.quantity}\n"
        return result[:-1]
