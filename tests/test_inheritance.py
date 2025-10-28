"""
Тесты для проверки наследования классов Smartphone и LawnGrass от Product.
"""
import pytest

from src.models import LawnGrass, Product, Smartphone


class TestSmartphoneInheritance:
    """Тесты для класса Smartphone"""

    def test_smartphone_initialization(self):
        """Тест инициализации смартфона"""
        smartphone = Smartphone(
            name="iPhone 15",
            description="Новый iPhone с чипом A17 Pro",
            price=100000.0,
            quantity=5,
            efficiency="A17 Pro",
            model="iPhone 15",
            memory=256,
            color="Черный"
        )

        # Проверяем наследование базовых атрибутов
        assert smartphone.name == "iPhone 15"
        assert smartphone.description == "Новый iPhone с чипом A17 Pro"
        assert smartphone.price == 100000.0
        assert smartphone.quantity == 5

        # Проверяем специфичные атрибуты
        assert smartphone.efficiency == "A17 Pro"
        assert smartphone.model == "iPhone 15"
        assert smartphone.memory == 256
        assert smartphone.color == "Черный"

    def test_smartphone_str_representation(self):
        """Тест строкового представления смартфона"""
        smartphone = Smartphone(
            name="Samsung Galaxy S24",
            description="Флагман Samsung",
            price=120000.0,
            quantity=3,
            efficiency="Snapdragon 8 Gen 3",
            model="Galaxy S24",
            memory=512,
            color="Белый"
        )

        str_repr = str(smartphone)
        assert "Samsung Galaxy S24" in str_repr
        assert "120000.0 руб." in str_repr
        assert "3 шт." in str_repr
        assert "Galaxy S24" in str_repr
        assert "512ГБ" in str_repr
        assert "Белый" in str_repr
        assert "Snapdragon 8 Gen 3" in str_repr

    def test_smartphone_addition(self):
        """Тест сложения смартфонов"""
        smartphone1 = Smartphone(
            name="iPhone 15", description="iPhone", price=100000.0, quantity=2,
            efficiency="A17 Pro", model="iPhone 15", memory=256, color="Черный"
        )
        smartphone2 = Smartphone(
            name="iPhone 15 Pro", description="iPhone Pro", price=120000.0, quantity=1,
            efficiency="A17 Pro", model="iPhone 15 Pro", memory=512, color="Белый"
        )

        # Сложение смартфонов
        result = smartphone1 + smartphone2
        expected = (100000.0 * 2) + (120000.0 * 1)  # 200000 + 120000 = 320000
        assert result == expected

    def test_smartphone_addition_with_wrong_type(self):
        """Тест сложения смартфона с неподходящим типом"""
        smartphone = Smartphone(
            name="iPhone 15", description="iPhone", price=100000.0, quantity=2,
            efficiency="A17 Pro", model="iPhone 15", memory=256, color="Черный"
        )
        product = Product("Обычный товар", "Описание", 50000.0, 1)

        with pytest.raises(TypeError, match="Смартфоны можно складывать только с другими смартфонами"):
            smartphone + product

    def test_smartphone_new_smartphone_classmethod(self):
        """Тест класс-метода new_smartphone"""
        smartphone_data = {
            'name': 'Xiaomi 14',
            'description': 'Флагман Xiaomi',
            'price': 80000.0,
            'quantity': 4,
            'efficiency': 'Snapdragon 8 Gen 3',
            'model': 'Xiaomi 14',
            'memory': 128,
            'color': 'Синий'
        }

        smartphone = Smartphone.new_smartphone(smartphone_data)

        assert smartphone.name == "Xiaomi 14"
        assert smartphone.price == 80000.0
        assert smartphone.efficiency == "Snapdragon 8 Gen 3"
        assert smartphone.memory == 128


class TestLawnGrassInheritance:
    """Тесты для класса LawnGrass"""

    def test_lawn_grass_initialization(self):
        """Тест инициализации газонной травы"""
        lawn_grass = LawnGrass(
            name="Газонная трава спортивная",
            description="Трава для спортивных площадок",
            price=500.0,
            quantity=100,
            country="Россия",
            germination_period=14,
            color="Зеленый"
        )

        # Проверяем наследование базовых атрибутов
        assert lawn_grass.name == "Газонная трава спортивная"
        assert lawn_grass.description == "Трава для спортивных площадок"
        assert lawn_grass.price == 500.0
        assert lawn_grass.quantity == 100

        # Проверяем специфичные атрибуты
        assert lawn_grass.country == "Россия"
        assert lawn_grass.germination_period == 14
        assert lawn_grass.color == "Зеленый"

    def test_lawn_grass_str_representation(self):
        """Тест строкового представления газонной травы"""
        lawn_grass = LawnGrass(
            name="Газонная трава декоративная",
            description="Декоративная трава",
            price=300.0,
            quantity=50,
            country="Германия",
            germination_period=21,
            color="Темно-зеленый"
        )

        str_repr = str(lawn_grass)
        assert "Газонная трава декоративная" in str_repr
        assert "300.0 руб." in str_repr
        assert "50 шт." in str_repr
        assert "Германия" in str_repr
        assert "21 дней" in str_repr
        assert "Темно-зеленый" in str_repr

    def test_lawn_grass_addition(self):
        """Тест сложения газонной травы"""
        lawn_grass1 = LawnGrass(
            name="Трава 1", description="Описание", price=200.0, quantity=10,
            country="Россия", germination_period=14, color="Зеленый"
        )
        lawn_grass2 = LawnGrass(
            name="Трава 2", description="Описание", price=300.0, quantity=5,
            country="Германия", germination_period=21, color="Темно-зеленый"
        )

        # Сложение газонной травы
        result = lawn_grass1 + lawn_grass2
        expected = (200.0 * 10) + (300.0 * 5)  # 2000 + 1500 = 3500
        assert result == expected

    def test_lawn_grass_addition_with_wrong_type(self):
        """Тест сложения газонной травы с неподходящим типом"""
        lawn_grass = LawnGrass(
            name="Трава", description="Описание", price=200.0, quantity=10,
            country="Россия", germination_period=14, color="Зеленый"
        )
        product = Product("Обычный товар", "Описание", 50000.0, 1)

        with pytest.raises(TypeError, match="Газонную траву можно складывать только с другой газонной травой"):
            lawn_grass + product

    def test_lawn_grass_new_lawn_grass_classmethod(self):
        """Тест класс-метода new_lawn_grass"""
        lawn_grass_data = {
            'name': 'Газонная трава универсальная',
            'description': 'Универсальная трава',
            'price': 400.0,
            'quantity': 75,
            'country': 'Франция',
            'germination_period': 18,
            'color': 'Светло-зеленый'
        }

        lawn_grass = LawnGrass.new_lawn_grass(lawn_grass_data)

        assert lawn_grass.name == "Газонная трава универсальная"
        assert lawn_grass.price == 400.0
        assert lawn_grass.country == "Франция"
        assert lawn_grass.germination_period == 18


class TestInheritanceBasics:
    """Тесты базовых принципов наследования"""

    def test_smartphone_is_product(self):
        """Тест что Smartphone является наследником Product"""
        smartphone = Smartphone(
            name="Test", description="Test", price=100.0, quantity=1,
            efficiency="Test", model="Test", memory=64, color="Test"
        )

        assert isinstance(smartphone, Product)
        assert isinstance(smartphone, Smartphone)
        assert not isinstance(smartphone, LawnGrass)

    def test_lawn_grass_is_product(self):
        """Тест что LawnGrass является наследником Product"""
        lawn_grass = LawnGrass(
            name="Test", description="Test", price=100.0, quantity=1,
            country="Test", germination_period=14, color="Test"
        )

        assert isinstance(lawn_grass, Product)
        assert isinstance(lawn_grass, LawnGrass)
        assert not isinstance(lawn_grass, Smartphone)

    def test_inheritance_methods(self):
        """Тест что наследники имеют доступ к методам родительского класса"""
        smartphone = Smartphone(
            name="Test", description="Test", price=100.0, quantity=2,
            efficiency="Test", model="Test", memory=64, color="Test"
        )

        # Проверяем доступ к методам родительского класса
        assert hasattr(smartphone, 'price')
        assert hasattr(smartphone, 'quantity')
        assert hasattr(smartphone, '__add__')
        assert hasattr(smartphone, '__str__')

        # Проверяем что методы работают
        assert smartphone.price == 100.0
        assert smartphone.quantity == 2


class TestCategoryProtection:
    """Тесты защиты метода add_product в Category"""

    def test_category_add_smartphone(self):
        """Тест добавления смартфона в категорию"""
        from src.models import Category

        category = Category("Телефоны", "Описание", [])
        smartphone = Smartphone(
            name="iPhone", description="Тест", price=100.0, quantity=1,
            efficiency="A17", model="iPhone", memory=64, color="Black"
        )

        # Должно работать без ошибок
        category.add_product(smartphone)
        assert len(category.get_products_list()) == 1

    def test_category_add_lawn_grass(self):
        """Тест добавления газонной травы в категорию"""
        from src.models import Category

        category = Category("Трава", "Описание", [])
        lawn_grass = LawnGrass(
            name="Трава", description="Тест", price=100.0, quantity=1,
            country="Россия", germination_period=14, color="Зеленый"
        )

        # Должно работать без ошибок
        category.add_product(lawn_grass)
        assert len(category.get_products_list()) == 1

    def test_category_add_product(self):
        """Тест добавления обычного продукта в категорию"""
        from src.models import Category

        category = Category("Товары", "Описание", [])
        product = Product("Товар", "Описание", 100.0, 1)

        # Должно работать без ошибок
        category.add_product(product)
        assert len(category.get_products_list()) == 1

    def test_category_add_non_product(self):
        """Тест попытки добавить не продукт в категорию"""
        from src.models import Category

        category = Category("Товары", "Описание", [])

        # Пытаемся добавить строку
        with pytest.raises(TypeError, match="В категорию можно добавлять только продукты"):
            category.add_product("Это строка")

        # Пытаемся добавить число
        with pytest.raises(TypeError, match="В категорию можно добавлять только продукты"):
            category.add_product(123)

        # Пытаемся добавить список
        with pytest.raises(TypeError, match="В категорию можно добавлять только продукты"):
            category.add_product([1, 2, 3])

        # Пытаемся добавить None
        with pytest.raises(TypeError, match="В категорию можно добавлять только продукты"):
            category.add_product(None)


class TestAdditionBetweenDifferentTypes:
    """Тесты сложения между разными типами продуктов"""

    def test_smartphone_and_lawn_grass_addition(self):
        """Тест сложения смартфона с газонной травой"""
        smartphone = Smartphone(
            name="iPhone", description="Тест", price=100.0, quantity=2,
            efficiency="A17", model="iPhone", memory=64, color="Black"
        )
        lawn_grass = LawnGrass(
            name="Трава", description="Тест", price=50.0, quantity=3,
            country="Россия", germination_period=14, color="Зеленый"
        )

        # Должна возникнуть ошибка TypeError
        with pytest.raises(TypeError):
            _ = smartphone + lawn_grass

        # И обратная операция тоже должна вызвать ошибку
        with pytest.raises(TypeError):
            _ = lawn_grass + smartphone

    def test_smartphone_and_product_addition(self):
        """Тест сложения смартфона с обычным продуктом"""
        smartphone = Smartphone(
            name="iPhone", description="Тест", price=100.0, quantity=2,
            efficiency="A17", model="iPhone", memory=64, color="Black"
        )
        product = Product("Товар", "Описание", 50.0, 3)

        # Должна возникнуть ошибка TypeError
        with pytest.raises(TypeError):
            _ = smartphone + product

    def test_lawn_grass_and_product_addition(self):
        """Тест сложения газонной травы с обычным продуктом"""
        lawn_grass = LawnGrass(
            name="Трава", description="Тест", price=50.0, quantity=3,
            country="Россия", germination_period=14, color="Зеленый"
        )
        product = Product("Товар", "Описание", 50.0, 3)

        # Должна возникнуть ошибка TypeError
        with pytest.raises(TypeError):
            _ = lawn_grass + product
