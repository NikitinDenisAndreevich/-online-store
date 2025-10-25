# Импорты для обратной совместимости
try:
    from .category import Category
    from .lawn_grass import LawnGrass
    from .product import Product
    from .smartphone import Smartphone
except ImportError:
    # Если относительные импорты не работают, используем абсолютные
    from category import Category
    from lawn_grass import LawnGrass
    from product import Product
    from smartphone import Smartphone

# Экспорт классов для удобства импорта
__all__ = ['Product', 'Category', 'Smartphone', 'LawnGrass']
