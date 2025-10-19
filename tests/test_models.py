import pytest

from models import Category, Product


@pytest.fixture(autouse=True)
def reset_counters():
    # Ensure each test starts with clean counters
    Category.category_count = 0
    Category.product_count = 0
    yield
    # Clean up not strictly necessary here


def test_product_initialization():
    product = Product("Test Phone", "Desc", 1000.0, 3)
    assert product.name == "Test Phone"
    assert product.description == "Desc"
    assert product.price == 1000.0
    assert product.quantity == 3


def test_category_initialization_and_products_list():
    p1 = Product("A", "a", 10.0, 1)
    p2 = Product("B", "b", 20.0, 2)
    category = Category("Phones", "All phones", [p1, p2])
    assert category.name == "Phones"
    assert category.description == "All phones"
    # Теперь products возвращает строку, а не список
    assert isinstance(category.products, str)
    assert "A, 10.0 руб. Остаток: 1 шт." in category.products
    assert "B, 20.0 руб. Остаток: 2 шт." in category.products


def test_counters_increment_on_category_creation():
    p1 = Product("A", "a", 10.0, 1)
    p2 = Product("B", "b", 20.0, 2)
    Category("Phones", "All phones", [p1, p2])
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_counters_accumulate_across_multiple_categories():
    p1 = Product("A", "a", 10.0, 1)
    p2 = Product("B", "b", 20.0, 2)
    p3 = Product("C", "c", 30.0, 3)
    Category("Phones", "All phones", [p1, p2])
    Category("Tablets", "All tablets", [p3])
    assert Category.category_count == 2
    assert Category.product_count == 3


# Тесты для новой функциональности

def test_private_products_attribute():
    """Тест приватного атрибута products"""
    p1 = Product("A", "a", 10.0, 1)
    p2 = Product("B", "b", 20.0, 2)
    category = Category("Phones", "All phones", [p1, p2])

    # Проверяем, что приватный атрибут недоступен напрямую
    with pytest.raises(AttributeError):
        _ = category.__products

    # Проверяем, что можно получить доступ через get_products_list()
    products_list = category.get_products_list()
    assert len(products_list) == 2
    assert products_list[0] == p1
    assert products_list[1] == p2


def test_add_product_method():
    """Тест метода add_product()"""
    category = Category("Phones", "All phones", [])
    p1 = Product("A", "a", 10.0, 1)

    # Изначально категория пустая
    assert len(category.get_products_list()) == 0
    assert category.products == "Товары отсутствуют"

    # Добавляем товар
    category.add_product(p1)
    assert len(category.get_products_list()) == 1
    assert category.get_products_list()[0] == p1
    assert "A, 10.0 руб. Остаток: 1 шт." in category.products

    # Добавляем еще один товар
    p2 = Product("B", "b", 20.0, 2)
    category.add_product(p2)
    assert len(category.get_products_list()) == 2
    assert "B, 20.0 руб. Остаток: 2 шт." in category.products


def test_products_getter_format():
    """Тест геттера products для форматированного вывода"""
    p1 = Product("Test Product", "Test Description", 100.0, 5)
    category = Category("Test Category", "Test Description", [p1])

    products_string = category.products
    assert isinstance(products_string, str)
    assert "Test Product, 100.0 руб. Остаток: 5 шт." in products_string

    # Тест для пустой категории
    empty_category = Category("Empty", "Empty", [])
    assert empty_category.products == "Товары отсутствуют"


def test_new_product_classmethod():
    """Тест класс-метода new_product"""
    product_data = {
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 150.0,
        'quantity': 3
    }

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == 'Test Product'
    assert product.description == 'Test Description'
    assert product.price == 150.0
    assert product.quantity == 3


def test_price_property_getter():
    """Тест геттера для свойства price"""
    product = Product("Test", "Test", 100.0, 1)
    assert product.price == 100.0

    # Проверяем, что приватный атрибут недоступен
    with pytest.raises(AttributeError):
        _ = product.__price


def test_price_property_setter_valid():
    """Тест сеттера для свойства price с валидными значениями"""
    product = Product("Test", "Test", 100.0, 1)

    # Устанавливаем положительную цену
    product.price = 200.0
    assert product.price == 200.0

    # Устанавливаем цену с плавающей точкой
    product.price = 150.5
    assert product.price == 150.5


def test_price_property_setter_invalid(capsys):
    """Тест сеттера для свойства price с невалидными значениями"""
    product = Product("Test", "Test", 100.0, 1)
    original_price = product.price

    # Пытаемся установить нулевую цену
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == original_price  # Цена не изменилась

    # Пытаемся установить отрицательную цену
    product.price = -50.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == original_price  # Цена не изменилась


def test_price_property_setter_negative(capsys):
    """Тест сеттера для свойства price с отрицательными значениями"""
    product = Product("Test", "Test", 100.0, 1)
    original_price = product.price

    # Пытаемся установить отрицательную цену
    product.price = -10.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == original_price


def test_add_product_updates_counter():
    """Тест обновления счетчика при добавлении товара"""
    category = Category("Test", "Test", [])
    initial_count = Category.product_count

    product = Product("Test", "Test", 100.0, 1)
    category.add_product(product)

    assert Category.product_count == initial_count + 1


def test_get_products_list_returns_copy():
    """Тест что get_products_list возвращает копию списка"""
    p1 = Product("A", "a", 10.0, 1)
    category = Category("Test", "Test", [p1])

    products_list1 = category.get_products_list()
    products_list2 = category.get_products_list()

    # Проверяем, что это разные объекты (копии)
    assert products_list1 is not products_list2
    # Но содержимое одинаковое
    assert products_list1 == products_list2
