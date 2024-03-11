# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import choice, randint
from pathlib import Path

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def generate_name(count: int = 1, file_name: str | Path = 'names.txt') -> None:
    """
    Генерирует и записывает имена в файл.

    Аргументы:
    count (int): Количество имен для генерации.
    file_name (str | Path): Путь к файлу, в который будут записаны имена.
    """
    for _ in range(count):
        first_char = choice([-1, 1])
        name = ''
        for _ in range(randint(MIN_LEN, MAX_LEN)):
            if first_char == -1:
                name += choice(CONSONANTS)
            else:
                name += choice(VOWELS)
            first_char *= -1
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(name.title() + '\n')


def generate_name2(count: int = 1, file_name: str | Path = 'names.txt') -> None:
    """
    Генерирует и записывает имена в файл, используя генератор списка.

    Аргументы:
    count (int): Количество имен для генерации.
    file_name (str | Path): Путь к файлу, в который будут записаны имена.
    """
    for _ in range(count):
        name = ''.join(
            choice(VOWELS) if i in (1, 4, 6)
            else choice(CONSONANTS)
            for i in range(randint(MIN_LEN, MAX_LEN))
        )

        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(name.title() + '\n')


__all__ = ['generate_name', 'generate_name2']

if __name__ == '__main__':
    generate_name(10, Path('names.txt'))

