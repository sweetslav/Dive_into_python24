# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён

from random import randint, choices
from string import ascii_lowercase, digits
from pathlib import Path
from os import chdir


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
        while True:
            file_name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            file_name = f'{file_name}.{extension}'
            if not Path(file_name).exists():
                break

        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(file_name, 'wb') as result_file:
            result_file.write(data)


def generate_files2(path: str | Path, **kwargs) -> None:
    """
    Генерирует файлы с указанными расширениями и количеством в указанной директории.

    Аргументы:
    path (str | Path): Путь к директории для сохранения файлов.
    **kwargs: Аргументы в формате "расширение: количество файлов".

    Возвращает:
    None: Функция ничего не возвращает.
    """
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True, exist_ok=True)
    chdir(path)

    for ext, count in kwargs.items():
        generate_files(extension=ext, count_files=count)


__all__ = ['generate_files', 'generate_files2']

if __name__ == '__main__':
    generate_files2(r'C:\Users\slavu\PycharmProjects\Dive_Into_Python\Lesson7', mp4=4, mov=4, mkv=4, jpg=4, jpeg=4, png=4)
