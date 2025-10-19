class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)


class Category:
    # Class-level counters shared across all instances
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = list(products)  # Приватный атрибут

        # Update class-level counters
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        """Добавляет товар в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает список товаров (только для чтения)"""
        return self.__products.copy()
