# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import randint, choices
from string import ascii_lowercase, digits


def generate_files(
    extension: str = 'bin',
    min_name: int = 6,
    max_name: int = 30,
    min_size: int = 256,
    max_size: int = 4096,
    count_files: int = 2
) -> None:
    """
    Генерирует файлы с случайными именами и данными указанного расширения.

    Аргументы:
    extension (str): Расширение файлов (по умолчанию 'bin').
    min_name (int): Минимальная длина имени файла (по умолчанию 6).
    max_name (int): Максимальная длина имени файла (по умолчанию 30).
    min_size (int): Минимальный размер файла в байтах (по умолчанию 256).
    max_size (int): Максимальный размер файла в байтах (по умолчанию 4096).
    count_files (int): Количество файлов для генерации (по умолчанию 2).

    Возвращает:
    None: Функция ничего не возвращает.
    """
    for _ in range(count_files):
        file_name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{file_name}.{extension}', 'wb') as result_file:
            result_file.write(data)


def generate_files2(**kwargs) -> None:
    """
    Генерирует файлы с указанными расширениями и количеством.

    Аргументы:
    **kwargs: Аргументы в формате "расширение: количество файлов".

    Возвращает:
    None: Функция ничего не возвращает.
    """
    for ext, count in kwargs.items():
        generate_files(extension=ext, count_files=count)


__all__ = ['generate_files', 'generate_files2']

if __name__ == '__main__':
    generate_files2(jpg=3, txt=2, bin=1)

