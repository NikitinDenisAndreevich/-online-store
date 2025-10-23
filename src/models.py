# Импорты для обратной совместимости
try:
    from .product import Product
    from .category import Category
except ImportError:
    # Если относительные импорты не работают, используем абсолютные
    from product import Product
    from category import Category

# Экспорт классов для удобства импорта
__all__ = ['Product', 'Category']
