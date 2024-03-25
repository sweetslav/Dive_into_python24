# Задание №1.
# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например, отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='error.log.', filemode='a', encoding='utf-8', level=logging.ERROR)


def get_div(a, b) -> float:
    try:
        res = a / b
    except ZeroDivisionError as e:
        logging.error(f'Ошибка деления на ноль в выражении {a} / {b}\n {e}')
        res = float('inf')
    finally:
        return res


if __name__ == '__main__':
    print(get_div(7, 3))