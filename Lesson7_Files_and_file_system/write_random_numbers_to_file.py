# Задание №1
# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random
from pathlib import Path

LOW_LIMIT = -1000
HIGH_LIMIT = 1000


def write_random_to_file(num_pairs: int, file_name: str | Path) -> None:
    """
    Записывает случайные целые и вещественные числа в файл.

    Аргументы:
    num_pairs (int): Количество пар случайных чисел для записи в файл.
    file_name (str | Path): Путь к файлу, в который будут записаны числа.

    Возвращает:
    None: Функция ничего не возвращает.
    """
    if isinstance(file_name, str):
        file_name = Path(file_name)

    if not file_name.parent.exists():
        file_name.parent.mkdir(parents=True)

    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(num_pairs):
            int_num = random.randint(LOW_LIMIT, HIGH_LIMIT)
            float_num = random.uniform(LOW_LIMIT, HIGH_LIMIT)
            file.write(f'{int_num:>4} | {float_num:>19}\n')


__all__ = ['write_random_to_file']

if __name__ == '__main__':
    write_random_to_file(10, 'numbers.txt')


