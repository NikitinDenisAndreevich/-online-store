from models import Category, Product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         """Смартфоны, как средство не только коммуникации,
                         но и получения дополнительных функций для удобства жизни""",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(f"Количество товаров в категории: {len(category1.get_products_list())}")
    print("Список товаров:")
    print(category1.products)
    print(Category.category_count)
    print(Category.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         """Современный телевизор, который позволяет наслаждаться просмотром,
                         станет вашим другом и помощником""",
                         [])

    # Добавляем товар с помощью метода add_product()
    category2.add_product(product4)

    print(category2.name)
    print(category2.description)
    print(f"Количество товаров в категории: {len(category2.get_products_list())}")
    print("Список товаров:")
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # Демонстрация добавления еще одного товара
    product5 = Product("Samsung 65\" QLED", "4K UHD, Smart TV", 150000.0, 3)
    category2.add_product(product5)
    print(f"После добавления товара: {len(category2.get_products_list())} товаров в категории")
    print("Обновленный список товаров:")
    print(category2.products)
    print(f"Общее количество товаров: {Category.product_count}")

    # Демонстрация использования класс-метода new_product
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ КЛАСС-МЕТОДА new_product")
    print("=" * 50)

    # Создаем товар из словаря
    product_data = {
        'name': 'MacBook Pro 16"',
        'description': 'M3 Pro, 18GB RAM, 512GB SSD',
        'price': 250000.0,
        'quantity': 2
    }

    product6 = Product.new_product(product_data)
    print("Создан товар через класс-метод:")
    print(f"Название: {product6.name}")
    print(f"Описание: {product6.description}")
    print(f"Цена: {product6.price} руб.")
    print(f"Количество: {product6.quantity} шт.")

    # Добавляем новый товар в категорию
    category2.add_product(product6)
    print("\nПосле добавления товара через класс-метод:")
    print(f"Количество товаров в категории: {len(category2.get_products_list())}")
    print("Финальный список товаров:")
    print(category2.products)
    print(f"Общее количество товаров: {Category.product_count}")

    # Демонстрация работы с приватным атрибутом price
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ С ПРИВАТНЫМ АТРИБУТОМ PRICE")
    print("=" * 50)

    # Создаем тестовый товар
    test_product = Product("Тестовый товар", "Для демонстрации", 1000.0, 5)
    print(f"Исходная цена товара: {test_product.price} руб.")

    # Пытаемся установить положительную цену
    test_product.price = 1500.0
    print(f"Цена после изменения на 1500: {test_product.price} руб.")

    # Пытаемся установить нулевую цену
    print("Попытка установить нулевую цену:")
    test_product.price = 0

    # Пытаемся установить отрицательную цену
    print("Попытка установить отрицательную цену:")
    test_product.price = -100

    # Проверяем, что цена не изменилась
    print(f"Цена после попыток установить недопустимые значения: {test_product.price} руб.")
