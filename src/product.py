try:
    from .base_product import BaseProduct
    from .logging_mixin import LoggingMixin
except ImportError:
    from base_product import BaseProduct
    from logging_mixin import LoggingMixin


class Product(LoggingMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)
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

    def __add__(self, other):
        """Складывает общую стоимость товара на складе с другим значением.

        Поддерживаемые варианты:
        - Product + Product -> сумма (price*quantity) по двум товарам
        - Product + (int|float) -> (price*quantity) + число
        """
        self_total = self.price * self.quantity
        if isinstance(other, Product):
            return self_total + other.price * other.quantity
        if isinstance(other, (int, float)):
            return self_total + other
        return NotImplemented

    def __radd__(self, other):
        """Поддержка суммирования, например sum([p1, p2], 0)."""
        if isinstance(other, (int, float)):
            return other + self.price * self.quantity
        if isinstance(other, Product):
            return self.__add__(other)
        return NotImplemented

    def get_total_value(self) -> float:
        """
        Возвращает общую стоимость товара на складе.

        Returns:
            float: Общая стоимость (цена * количество)
        """
        return self.price * self.quantity

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
