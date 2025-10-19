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

    def get_products_list(self):
        """Возвращает список объектов товаров (только для чтения)"""
        return self.__products.copy()

    @property
    def products(self):
        """Возвращает список товаров в формате строк"""
        if not self.__products:
            return "Товары отсутствуют"
        
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        
        return "\n".join(products_list)
