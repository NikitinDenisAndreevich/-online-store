try:
    from .product import Product
except ImportError:
    from product import Product


class Category:
    # Class-level counters shared across all instances
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = list(products)  # Приватный атрибут

        # Update class-level counters
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию.
        Защищен от добавления объектов, не являющихся продуктами или их наследниками.
        """
        # Проверяем, что объект является продуктом или его наследником
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только продукты или их наследников")

        self.__products.append(product)
        Category.product_count += 1

    def get_products_list(self):
        """Возвращает список объектов товаров (только для чтения)"""
        return self.__products.copy()

    @property
    def products(self):
        """Возвращает список товаров в формате строк"""
        if not self.__products:
            return "Товары отсутствуют"

        products_list = []
        for product in self.__products:
            products_list.append(str(product))

        return "\n".join(products_list)

    def average_price(self):
        """
        Подсчитывает средний ценник всех товаров в категории.

        Returns:
            float: Средняя цена товаров. Возвращает 0, если в категории нет товаров.
        """
        try:
            total_price = sum(product.price for product in self.__products)
            average = total_price / len(self.__products)
            return average
        except ZeroDivisionError:
            return 0
