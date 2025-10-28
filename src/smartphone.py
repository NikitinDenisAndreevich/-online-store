try:
    from .product import Product
except ImportError:
    from product import Product


class Smartphone(Product):
    """
    Класс для представления смартфона.
    Наследуется от класса Product и добавляет специфичные для смартфона свойства.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: int, color: str):
        """
        Инициализация смартфона.

        Args:
            name (str): Название смартфона
            description (str): Описание смартфона
            price (float): Цена смартфона
            quantity (int): Количество на складе
            efficiency (str): Производительность смартфона
            model (str): Модель смартфона
            memory (int): Объем встроенной памяти в ГБ
            color (str): Цвет смартфона
        """
        # Вызываем конструктор родительского класса
        super().__init__(name, description, price, quantity)

        # Добавляем специфичные для смартфона атрибуты
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """
        Строковое представление смартфона.
        Расширяет базовое представление Product дополнительной информацией.
        """
        base_info = super().__str__()
        return f"{base_info} | {self.model} | {self.memory}ГБ | {self.color} | {self.efficiency}"

    def __add__(self, other):
        """
        Переопределяем метод сложения для смартфонов.
        Складывает только смартфоны между собой.
        """
        if type(other) == type(self):  # noqa: E721
            return super().__add__(other)
        else:
            raise TypeError("Смартфоны можно складывать только с другими смартфонами")

    @classmethod
    def new_smartphone(cls, smartphone_data: dict):
        """
        Создает новый объект Smartphone из словаря с параметрами.

        Args:
            smartphone_data (dict): Словарь с ключами 'name', 'description', 'price',
                                  'quantity', 'efficiency', 'model', 'memory', 'color'

        Returns:
            Smartphone: Новый объект класса Smartphone
        """
        return cls(
            name=smartphone_data['name'],
            description=smartphone_data['description'],
            price=smartphone_data['price'],
            quantity=smartphone_data['quantity'],
            efficiency=smartphone_data['efficiency'],
            model=smartphone_data['model'],
            memory=smartphone_data['memory'],
            color=smartphone_data['color']
        )
