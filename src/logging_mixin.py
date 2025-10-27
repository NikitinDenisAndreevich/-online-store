class LoggingMixin:
    """
    Миксин для логирования создания объектов.
    Печатает в консоль информацию о том, от какого класса и с какими параметрами был создан объект.
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация с логированием.
        Вызывает родительский __init__ и затем выводит информацию о создании объекта.
        """
        # Вызываем родительский __init__ если он есть
        # Проверяем есть ли родительский класс с __init__ кроме object
        mro = self.__class__.__mro__
        for cls in mro[1:]:  # Пропускаем текущий класс
            if hasattr(cls, '__init__') and cls.__init__ is not object.__init__ and cls is not LoggingMixin:
                super().__init__(*args, **kwargs)
                break

        # Получаем имя класса
        class_name = self.__class__.__name__

        # Формируем строку с параметрами
        params = []

        # Добавляем позиционные аргументы
        if args:
            params.extend([repr(arg) for arg in args])

        # Добавляем именованные аргументы
        if kwargs:
            params.extend([f"{key}={repr(value)}" for key, value in kwargs.items()])

        # Формируем итоговую строку
        params_str = ", ".join(params)

        # Выводим информацию о создании объекта
        print(f"{class_name}({params_str})")
