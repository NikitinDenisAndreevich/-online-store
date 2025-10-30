import pytest

from src.models import Category, Product


@pytest.fixture(autouse=True)
def reset_counters():
    # Ensure each tests starts with clean counters
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


def test_product_addition():
    """Тест сложения продуктов - проверка метода __add__"""
    # Создаем продукты как в примере из задания
    product_a = Product("a", "Товар A", 100.0, 10)  # цена 100, количество 10
    product_b = Product("b", "Товар B", 200.0, 2)   # цена 200, количество 2

    # Проверяем сложение двух продуктов
    result = product_a + product_b
    expected = 100 * 10 + 200 * 2  # 1000 + 400 = 1400
    assert result == expected

    # Проверяем сложение продукта с числом
    result_with_number = product_a + 500
    expected_with_number = 100 * 10 + 500  # 1000 + 500 = 1500
    assert result_with_number == expected_with_number

    # Проверяем коммутативность (product + number = number + product)
    result_reverse = 500 + product_a
    assert result_reverse == expected_with_number


def test_product_addition_edge_cases():
    """Тест граничных случаев для сложения продуктов"""
    product = Product("Test", "Test", 50.0, 3)

    # Сложение с нулем
    assert product + 0 == 150.0
    assert 0 + product == 150.0

    # Сложение с отрицательным числом
    assert product + (-50) == 100.0
    assert (-50) + product == 100.0

    # Нельзя создать продукт с нулевым количеством
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Empty", "Empty", 100.0, 0)


def test_category_str_shows_total_quantity():
    """__str__ категории должен показывать сумму quantity всех товаров"""
    p1 = Product("X", "x", 10.0, 3)
    p2 = Product("Y", "y", 20.0, 7)
    category = Category("Mix", "desc", [p1, p2])

    # total quantity = 3 + 7 = 10
    s = str(category)
    assert "Mix, количество продуктов: 10 шт." in s


# Тесты для новой функциональности (Задание 17.1)

def test_product_zero_quantity_raises_value_error():
    """Тест что создание товара с нулевым количеством вызывает ValueError"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test Product", "Description", 100.0, 0)


def test_category_average_price_with_products():
    """Тест метода average_price с товарами в категории"""
    p1 = Product("Product 1", "Desc 1", 100.0, 5)
    p2 = Product("Product 2", "Desc 2", 200.0, 3)
    p3 = Product("Product 3", "Desc 3", 300.0, 2)
    category = Category("Test Category", "Description", [p1, p2, p3])

    # Средняя цена = (100 + 200 + 300) / 3 = 200.0
    assert category.middle_price() == 200.0


def test_category_average_price_with_single_product():
    """Тест метода average_price с одним товаром в категории"""
    p1 = Product("Product 1", "Desc 1", 150.0, 10)
    category = Category("Test Category", "Description", [p1])

    assert category.middle_price() == 150.0


def test_category_average_price_empty_category():
    """Тест метода average_price с пустой категорией (деление на ноль)"""
    category = Category("Empty Category", "Description", [])

    # Должен вернуть 0 при пустой категории
    assert category.middle_price() == 0


def test_category_average_price_with_different_prices():
    """Тест метода average_price с товарами разных цен"""
    p1 = Product("Product 1", "Desc 1", 10.0, 2)
    p2 = Product("Product 2", "Desc 2", 20.0, 3)
    category = Category("Test Category", "Description", [p1, p2])

    # Средняя цена = (10 + 20) / 2) = 15.0
    assert category.middle_price() == 15.0
