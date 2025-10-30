try:
    from .product import Product
except ImportError:
    from product import Product


class LawnGrass(Product):
    """
    Класс для представления газонной травы.
    Наследуется от класса Product и добавляет специфичные для газонной травы свойства.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        """
        Инициализация газонной травы.

        Args:
            name (str): Название газонной травы
            description (str): Описание газонной травы
            price (float): Цена газонной травы
            quantity (int): Количество на складе
            country (str): Страна-производитель
            germination_period (int): Срок прорастания в днях
            color (str): Цвет газонной травы
        """
        # Вызываем конструктор родительского класса
        super().__init__(name, description, price, quantity)

        # Добавляем специфичные для газонной травы атрибуты
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """
        Строковое представление газонной травы.
        Расширяет базовое представление Product дополнительной информацией.
        """
        base_info = super().__str__()
        return f"{base_info} | {self.country} | {self.germination_period} дней | {self.color}"

    def __add__(self, other):
        """
        Переопределяем метод сложения для газонной травы.
        Складывает только газонную траву между собой.
        """
        if type(other) == type(self):  # noqa: E721
            return super().__add__(other)
        else:
            raise TypeError("Газонную траву можно складывать только с другой газонной травой")

    @classmethod
    def new_lawn_grass(cls, lawn_grass_data: dict):
        """
        Создает новый объект LawnGrass из словаря с параметрами.

        Args:
            lawn_grass_data (dict): Словарь с ключами 'name', 'description', 'price',
                                  'quantity', 'country', 'germination_period', 'color'

        Returns:
            LawnGrass: Новый объект класса LawnGrass
        """
        return cls(
            name=lawn_grass_data['name'],
            description=lawn_grass_data['description'],
            price=lawn_grass_data['price'],
            quantity=lawn_grass_data['quantity'],
            country=lawn_grass_data['country'],
            germination_period=lawn_grass_data['germination_period'],
            color=lawn_grass_data['color']
        )
