from sys import modules


def introspection_info(obj):
    # Определяем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = dir(obj)

    # Фильтруем атрибуты, чтобы оставить только 'методы' (функции) и не включать магические методы
    methods = [attr for attr in attributes if callable(getattr(obj, attr)) and not attr.startswith('__')]

    # Получаем модуль, к которому принадлежит объект
    module = getattr(obj.__class__, '__module__', '__main__')

    # Создаем словарь с информацией об объекте
    result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }

    # Можно добавить другие интересные свойства объекта, например, если это класс
    if isinstance(obj, type):
        result['is_class'] = True
        result['base_classes'] = [base.__name__ for base in obj.__bases__]
    else:
        result['is_class'] = False

    return result


# Пример использования
number_info1 = introspection_info(modules)
number_info2 = introspection_info(2)
number_info3 = introspection_info('2')
number_info4 = introspection_info(SyntaxError)
print(f'{number_info1}\n{number_info2}\n{number_info3}\n{number_info4}')
