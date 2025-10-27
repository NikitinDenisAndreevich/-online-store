# Импорты для обратной совместимости
try:
    from .base_product import BaseProduct
    from .category import Category
    from .lawn_grass import LawnGrass
    from .logging_mixin import LoggingMixin
    from .product import Product
    from .smartphone import Smartphone
except ImportError:
    # Если относительные импорты не работают, используем абсолютные
    from base_product import BaseProduct
    from category import Category
    from lawn_grass import LawnGrass
    from logging_mixin import LoggingMixin
    from product import Product
    from smartphone import Smartphone

# Экспорт классов для удобства импорта
__all__ = ['BaseProduct', 'Product', 'Category', 'Smartphone', 'LawnGrass', 'LoggingMixin']
