import inspect

def strict(func):
    def wrapper(*args, **kwargs):
        # Получаем список параметров функции, например: func(a: int, b: str)
        # Возвращает список имен параметров: ['a', 'b']
        func_params = list(inspect.signature(func).parameters)

        # Получаем аннотации типов из прототипа функции
        # Возвращает словарь: {'a': <class 'int'>, 'b': <class 'str'>}
        annotations = func.__annotations__ 

        for index, value in enumerate(args):
            # Получаем имя параметра по его индексу из списка параметров
            param_name = func_params[index]

            # Получаем ожидаемый тип параметра по его имени из аннотаций
            expected_type = annotations.get(param_name)

            # Если тип указан и тип значения не соответствует ожидаемому — вызываем ошибку
            if expected_type is not None and not isinstance(value, expected_type):
                raise TypeError(
                    f"Аргумент '{param_name}' должен быть типа {expected_type.__name__}, "
                    f"а не {type(value).__name__}"
                )
            
        # Вызываем оригинальную функцию с переданными аргументами
        return func(*args, **kwargs)

    return wrapper
