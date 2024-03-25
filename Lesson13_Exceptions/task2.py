# Задание №2.
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

# def my_get(my_dict, key, default=None) -> dict:
#     try:
#         return my_dict[key]
#     except KeyError:
#         return default

def my_get(my_dict, key, default=None) -> dict:
    result = default
    try:
        result = my_dict[key]
    except KeyError:
        pass
    return result



if __name__ == '__main__':
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    print(my_get(test_dict, key='t', default='Invalid key, try again'))
