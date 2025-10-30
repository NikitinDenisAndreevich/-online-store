"""
Тесты для новой функциональности: абстрактный класс BaseProduct и миксин LoggingMixin.
"""
from abc import ABC

import pytest

from src.models import (BaseProduct, LawnGrass, LoggingMixin, Product,
                        Smartphone)


class TestBaseProduct:
    """Тесты для абстрактного класса BaseProduct"""

    def test_base_product_is_abstract(self):
        """Тест что BaseProduct является абстрактным классом"""
        assert issubclass(BaseProduct, ABC)

        # Нельзя создать экземпляр абстрактного класса
        with pytest.raises(TypeError):
            BaseProduct("Test", "Test", 100.0, 1)

    def test_product_inherits_from_base_product(self):
        """Тест что Product наследуется от BaseProduct"""
        assert issubclass(Product, BaseProduct)

        # Product можно создать
        product = Product("Test", "Test", 100.0, 1)
        assert isinstance(product, BaseProduct)

    def test_smartphone_inherits_from_base_product(self):
        """Тест что Smartphone наследуется от BaseProduct через Product"""
        assert issubclass(Smartphone, BaseProduct)

        smartphone = Smartphone(
            name="Test", description="Test", price=100.0, quantity=1,
            efficiency="Test", model="Test", memory=64, color="Test"
        )
        assert isinstance(smartphone, BaseProduct)

    def test_lawn_grass_inherits_from_base_product(self):
        """Тест что LawnGrass наследуется от BaseProduct через Product"""
        assert issubclass(LawnGrass, BaseProduct)

        lawn_grass = LawnGrass(
            name="Test", description="Test", price=100.0, quantity=1,
            country="Test", germination_period=14, color="Test"
        )
        assert isinstance(lawn_grass, BaseProduct)

    def test_base_product_abstract_methods(self):
        """Тест что BaseProduct определяет все необходимые абстрактные методы"""
        abstract_methods = BaseProduct.__abstractmethods__

        expected_methods = {
            '__init__', '__str__', '__add__', 'price', 'get_total_value'
        }

        assert abstract_methods == expected_methods


class TestLoggingMixin:
    """Тесты для миксина LoggingMixin"""

    def test_logging_mixin_can_be_instantiated(self):
        """Тест что LoggingMixin можно использовать как миксин"""
        class TestClass(LoggingMixin):
            def __init__(self, name, value):
                super().__init__(name=name, value=value)
                self.name = name
                self.value = value

        # Создание объекта должно работать
        obj = TestClass("test", 42)
        assert obj.name == "test"
        assert obj.value == 42

    def test_logging_mixin_output(self, capsys):
        """Тест что LoggingMixin выводит информацию о создании объекта"""
        class TestClass(LoggingMixin):
            def __init__(self, name, value):
                super().__init__(name=name, value=value)
                self.name = name
                self.value = value

        # Создаем объект
        TestClass("test", 42)

        # Проверяем вывод
        captured = capsys.readouterr()
        assert "TestClass(name='test', value=42)" in captured.out

    def test_logging_mixin_with_positional_args(self, capsys):
        """Тест LoggingMixin с позиционными аргументами"""
        class TestClass(LoggingMixin):
            def __init__(self, name, value):
                super().__init__(name, value)
                self.name = name
                self.value = value

        # Создаем объект
        TestClass("test", 42)

        # Проверяем вывод
        captured = capsys.readouterr()
        assert "TestClass('test', 42)" in captured.out

    def test_logging_mixin_with_mixed_args(self, capsys):
        """Тест LoggingMixin со смешанными аргументами"""
        class TestClass(LoggingMixin):
            def __init__(self, name, value, extra=None):
                super().__init__(name, value, extra=extra)
                self.name = name
                self.value = value
                self.extra = extra

        # Создаем объект
        TestClass("test", 42, extra="additional")

        # Проверяем вывод
        captured = capsys.readouterr()
        assert "TestClass('test', 42, extra='additional')" in captured.out


class TestProductWithNewFeatures:
    """Тесты для Product с новой функциональностью"""

    def test_product_inherits_logging_mixin(self):
        """Тест что Product наследуется от LoggingMixin"""
        assert issubclass(Product, LoggingMixin)

    def test_product_creation_logging(self, capsys):
        """Тест что создание Product выводит информацию в консоль"""
        Product("Продукт1", "Описание продукта", 1200, 10)

        # Проверяем вывод
        captured = capsys.readouterr()
        assert "Product('Продукт1', 'Описание продукта', 1200, 10)" in captured.out

    def test_product_get_total_value(self):
        """Тест метода get_total_value"""
        product = Product("Test", "Test", 100.0, 5)

        total_value = product.get_total_value()
        assert total_value == 500.0  # 100.0 * 5

    def test_product_get_total_value_zero_quantity(self):
        """Тест что нельзя создать продукт с нулевым количеством"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Test", "Test", 100.0, 0)

    def test_product_get_total_value_after_price_change(self):
        """Тест метода get_total_value после изменения цены"""
        product = Product("Test", "Test", 100.0, 5)

        # Изначальная стоимость
        assert product.get_total_value() == 500.0

        # Изменяем цену
        product.price = 200.0

        # Новая стоимость
        assert product.get_total_value() == 1000.0  # 200.0 * 5


class TestSmartphoneWithNewFeatures:
    """Тесты для Smartphone с новой функциональностью"""

    def test_smartphone_creation_logging(self, capsys):
        """Тест что создание Smartphone выводит информацию в консоль"""
        Smartphone(
            name="iPhone 15", description="Новый iPhone", price=100000.0, quantity=2,
            efficiency="A17 Pro", model="iPhone 15", memory=256, color="Черный"
        )

        # Проверяем вывод
        captured = capsys.readouterr()
        assert "Smartphone('iPhone 15', 'Новый iPhone', 100000.0, 2)" in captured.out

    def test_smartphone_get_total_value(self):
        """Тест метода get_total_value для Smartphone"""
        smartphone = Smartphone(
            name="Test", description="Test", price=1000.0, quantity=3,
            efficiency="Test", model="Test", memory=64, color="Test"
        )

        total_value = smartphone.get_total_value()
        assert total_value == 3000.0  # 1000.0 * 3


class TestLawnGrassWithNewFeatures:
    """Тесты для LawnGrass с новой функциональностью"""

    def test_lawn_grass_creation_logging(self, capsys):
        """Тест что создание LawnGrass выводит информацию в консоль"""
        LawnGrass(
            name="Газонная трава", description="Трава для газона", price=500.0, quantity=20,
            country="Россия", germination_period=14, color="Зеленый"
        )

        # Проверяем вывод
        captured = capsys.readouterr()
        assert "LawnGrass('Газонная трава', 'Трава для газона', 500.0, 20)" in captured.out

    def test_lawn_grass_get_total_value(self):
        """Тест метода get_total_value для LawnGrass"""
        lawn_grass = LawnGrass(
            name="Test", description="Test", price=200.0, quantity=10,
            country="Test", germination_period=14, color="Test"
        )

        total_value = lawn_grass.get_total_value()
        assert total_value == 2000.0  # 200.0 * 10


class TestMultipleInheritance:
    """Тесты множественного наследования"""

    def test_product_inheritance_chain(self):
        """Тест цепочки наследования Product"""
        # Product наследуется от BaseProduct и LoggingMixin
        assert issubclass(Product, BaseProduct)
        assert issubclass(Product, LoggingMixin)

        # Проверяем MRO (Method Resolution Order)
        mro = Product.__mro__
        assert Product in mro
        assert BaseProduct in mro
        assert LoggingMixin in mro

    def test_smartphone_inheritance_chain(self):
        """Тест цепочки наследования Smartphone"""
        # Smartphone наследуется от Product, который наследуется от BaseProduct и LoggingMixin
        assert issubclass(Smartphone, Product)
        assert issubclass(Smartphone, BaseProduct)
        assert issubclass(Smartphone, LoggingMixin)

    def test_lawn_grass_inheritance_chain(self):
        """Тест цепочки наследования LawnGrass"""
        # LawnGrass наследуется от Product, который наследуется от BaseProduct и LoggingMixin
        assert issubclass(LawnGrass, Product)
        assert issubclass(LawnGrass, BaseProduct)
        assert issubclass(LawnGrass, LoggingMixin)

    def test_inheritance_methods_work(self):
        """Тест что методы из всех родительских классов работают"""
        product = Product("Test", "Test", 100.0, 5)

        # Методы из BaseProduct
        assert hasattr(product, 'get_total_value')
        assert product.get_total_value() == 500.0

        # Методы из LoggingMixin (проверяем что __init__ был вызван)
        assert product.name == "Test"
        assert product.price == 100.0
        assert product.quantity == 5


class TestBackwardCompatibility:
    """Тесты обратной совместимости"""

    def test_existing_product_functionality(self):
        """Тест что существующая функциональность Product работает"""
        product = Product("Test", "Test", 100.0, 5)

        # Проверяем все существующие методы и свойства
        assert product.name == "Test"
        assert product.description == "Test"
        assert product.price == 100.0
        assert product.quantity == 5

        # Проверяем строковое представление
        str_repr = str(product)
        assert "Test" in str_repr
        assert "100.0 руб." in str_repr
        assert "5 шт." in str_repr

        # Проверяем сложение
        product2 = Product("Test2", "Test2", 200.0, 2)
        result = product + product2
        assert result == 900.0  # (100*5) + (200*2) = 500 + 400 = 900

    def test_existing_smartphone_functionality(self):
        """Тест что существующая функциональность Smartphone работает"""
        smartphone = Smartphone(
            name="iPhone", description="iPhone", price=1000.0, quantity=2,
            efficiency="A17", model="iPhone", memory=256, color="Black"
        )

        # Проверяем все существующие методы и свойства
        assert smartphone.name == "iPhone"
        assert smartphone.price == 1000.0
        assert smartphone.efficiency == "A17"
        assert smartphone.model == "iPhone"
        assert smartphone.memory == 256
        assert smartphone.color == "Black"

    def test_existing_lawn_grass_functionality(self):
        """Тест что существующая функциональность LawnGrass работает"""
        lawn_grass = LawnGrass(
            name="Трава", description="Трава", price=200.0, quantity=10,
            country="Россия", germination_period=14, color="Зеленый"
        )

        # Проверяем все существующие методы и свойства
        assert lawn_grass.name == "Трава"
        assert lawn_grass.price == 200.0
        assert lawn_grass.country == "Россия"
        assert lawn_grass.germination_period == 14
        assert lawn_grass.color == "Зеленый"
