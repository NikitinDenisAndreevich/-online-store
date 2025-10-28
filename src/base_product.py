from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    Определяет общую функциональность, которая должна быть у каждого продукта.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Абстрактный конструктор для инициализации продукта.

        Args:
            name (str): Название продукта
            description (str): Описание продукта
            price (float): Цена продукта
            quantity (int): Количество на складе
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Абстрактный метод для строкового представления продукта.

        Returns:
            str: Строковое представление продукта
        """
        pass

    @abstractmethod
    def __add__(self, other):
        """
        Абстрактный метод для сложения продуктов.

        Args:
            other: Другой объект для сложения

        Returns:
            Результат сложения
        """
        pass

    @property
    @abstractmethod
    def price(self):
        """
        Абстрактное свойство для получения цены продукта.

        Returns:
            float: Цена продукта
        """
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """
        Абстрактный сеттер для установки цены продукта.

        Args:
            value: Новое значение цены
        """
        pass

    @abstractmethod
    def get_total_value(self) -> float:
        """
        Абстрактный метод для получения общей стоимости товара на складе.

        Returns:
            float: Общая стоимость (цена * количество)
        """
        pass
