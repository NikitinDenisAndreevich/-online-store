class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = float(price)  # Приватный атрибут
        self.quantity = int(quantity)

    @property
    def price(self):
        """Геттер для атрибута price"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для атрибута price с проверкой на положительное значение"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = float(value)

    def __str__(self):
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Создает новый объект Product из словаря с параметрами

        Args:
            product_data (dict): Словарь с ключами 'name', 'description', 'price', 'quantity'

        Returns:
            Product: Новый объект класса Product
        """
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )


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

    def __str__(self):
        """Строковое представление категории"""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

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
            products_list.append(str(product))

        return "\n".join(products_list)
