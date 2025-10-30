"""
Пример использования классов-наследников Smartphone и LawnGrass.
Демонстрирует наследование от класса Product и специфичные возможности.
"""
try:
    from .models import Category, LawnGrass, Product, Smartphone
except ImportError:
    from models import Category, LawnGrass, Product, Smartphone

if __name__ == '__main__':
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ НАСЛЕДОВАНИЯ: СМАРТФОНЫ И ГАЗОННАЯ ТРАВА")
    print("=" * 60)

    # Создаем обычные товары
    print("\n1. СОЗДАНИЕ ОБЫЧНЫХ ТОВАРОВ")
    print("-" * 40)

    product1 = Product("Обычный товар", "Описание обычного товара", 1000.0, 10)
    print(f"Обычный товар: {product1}")

    # Создаем смартфоны
    print("\n2. СОЗДАНИЕ СМАРТФОНОВ")
    print("-" * 40)

    smartphone1 = Smartphone(
        name="iPhone 15 Pro",
        description="Флагманский iPhone с чипом A17 Pro",
        price=120000.0,
        quantity=3,
        efficiency="A17 Pro",
        model="iPhone 15 Pro",
        memory=512,
        color="Титан"
    )

    smartphone2 = Smartphone(
        name="Samsung Galaxy S24 Ultra",
        description="Флагман Samsung с S Pen",
        price=130000.0,
        quantity=2,
        efficiency="Snapdragon 8 Gen 3",
        model="Galaxy S24 Ultra",
        memory=1024,
        color="Титан черный"
    )

    smartphone3 = Smartphone(
        name="Xiaomi 14 Pro",
        description="Флагман Xiaomi с Leica камерой",
        price=80000.0,
        quantity=5,
        efficiency="Snapdragon 8 Gen 3",
        model="Xiaomi 14 Pro",
        memory=256,
        color="Белый"
    )

    print(f"Смартфон 1: {smartphone1}")
    print(f"Смартфон 2: {smartphone2}")
    print(f"Смартфон 3: {smartphone3}")

    # Создаем газонную траву
    print("\n3. СОЗДАНИЕ ГАЗОННОЙ ТРАВЫ")
    print("-" * 40)

    lawn_grass1 = LawnGrass(
        name="Газонная трава спортивная",
        description="Трава для спортивных площадок и футбольных полей",
        price=800.0,
        quantity=50,
        country="Россия",
        germination_period=14,
        color="Темно-зеленый"
    )

    lawn_grass2 = LawnGrass(
        name="Газонная трава декоративная",
        description="Декоративная трава для садов и парков",
        price=600.0,
        quantity=30,
        country="Германия",
        germination_period=21,
        color="Светло-зеленый"
    )

    lawn_grass3 = LawnGrass(
        name="Газонная трава универсальная",
        description="Универсальная трава для любых целей",
        price=500.0,
        quantity=100,
        country="Франция",
        germination_period=18,
        color="Зеленый"
    )

    print(f"Газонная трава 1: {lawn_grass1}")
    print(f"Газонная трава 2: {lawn_grass2}")
    print(f"Газонная трава 3: {lawn_grass3}")

    # Создаем категории
    print("\n4. СОЗДАНИЕ КАТЕГОРИЙ")
    print("-" * 40)

    smartphones_category = Category(
        name="Смартфоны",
        description="Современные смартфоны с передовыми технологиями",
        products=[smartphone1, smartphone2, smartphone3]
    )

    lawn_grass_category = Category(
        name="Газонная трава",
        description="Качественная газонная трава для различных целей",
        products=[lawn_grass1, lawn_grass2, lawn_grass3]
    )

    print(f"Категория смартфонов: {smartphones_category}")
    print(f"Категория газонной травы: {lawn_grass_category}")

    # Демонстрация сложения
    print("\n5. ДЕМОНСТРАЦИЯ СЛОЖЕНИЯ")
    print("-" * 40)

    # Сложение смартфонов
    smartphone_total = smartphone1 + smartphone2
    print(f"Общая стоимость смартфонов 1 и 2: {smartphone_total} руб.")

    # Сложение газонной травы
    lawn_grass_total = lawn_grass1 + lawn_grass2
    print(f"Общая стоимость газонной травы 1 и 2: {lawn_grass_total} руб.")

    # Демонстрация класс-методов
    print("\n6. ДЕМОНСТРАЦИЯ КЛАСС-МЕТОДОВ")
    print("-" * 40)

    # Создание смартфона через класс-метод
    smartphone_data = {
        'name': 'Google Pixel 8 Pro',
        'description': 'Флагман Google с ИИ',
        'price': 90000.0,
        'quantity': 4,
        'efficiency': 'Google Tensor G3',
        'model': 'Pixel 8 Pro',
        'memory': 256,
        'color': 'Обсидиан'
    }

    smartphone4 = Smartphone.new_smartphone(smartphone_data)
    print(f"Смартфон через класс-метод: {smartphone4}")

    # Создание газонной травы через класс-метод
    lawn_grass_data = {
        'name': 'Газонная трава премиум',
        'description': 'Премиальная газонная трава',
        'price': 1200.0,
        'quantity': 25,
        'country': 'Италия',
        'germination_period': 12,
        'color': 'Изумрудный'
    }

    lawn_grass4 = LawnGrass.new_lawn_grass(lawn_grass_data)
    print(f"Газонная трава через класс-метод: {lawn_grass4}")

    # Демонстрация ошибок при сложении разных типов
    print("\n7. ДЕМОНСТРАЦИЯ ОШИБОК ПРИ СЛОЖЕНИИ")
    print("-" * 40)

    try:
        wrong_addition = smartphone1 + lawn_grass1
    except TypeError as e:
        print(f"Ошибка при сложении смартфона и газонной травы: {e}")

    try:
        wrong_addition = smartphone1 + product1
    except TypeError as e:
        print(f"Ошибка при сложении смартфона и обычного товара: {e}")

    # Статистика
    print("\n8. СТАТИСТИКА")
    print("-" * 40)
    print(f"Общее количество категорий: {Category.category_count}")
    print(f"Общее количество товаров: {Category.product_count}")

    print("\nТовары в категории 'Смартфоны':")
    print(smartphones_category.products)

    print("\nТовары в категории 'Газонная трава':")
    print(lawn_grass_category.products)

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)
