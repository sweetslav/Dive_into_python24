# Задание №6
# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 5 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle
from pathlib import Path

__all__ = ['pickle_to_csv']


def pickle_to_csv(path: Path) -> None:
    """
    Преобразует данные из файла формата pickle в CSV-файл.

    Аргументы:
    path (Path): Путь к файлу формата pickle.

    Возвращает:
    None: Функция ничего не возвращает.
    """
    with open(path, "rb") as f_r:
        data = pickle.load(f_r)

    with open(f'{path.stem}.csv', "w", newline='', encoding='utf-8') as f_w:
        keys = data[0].keys()
        csv_writer = csv.DictWriter(f_w, fieldnames=keys, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)


if __name__ == '__main__':
    pickle_to_csv(Path('users.pickle'))
