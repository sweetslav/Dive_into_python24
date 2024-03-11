# Задание №7
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle
from pathlib import Path

__all__ = ['csv_to_pickle']


def csv_to_pickle(csv_file: Path) -> None:
    """
    Преобразует данные из CSV-файла в формат pickle и сохраняет их.

    Аргументы:
    csv_file (Path): Путь к CSV-файлу.

    Возвращает:
    None: Функция ничего не возвращает.
    """
    pickle_list = []
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile, dialect='excel-tab')
        for i, row in enumerate(data):
            if not i:
                keys = row
            else:
                pickle_dict = dict(zip(keys, row))
                pickle_list.append(pickle_dict)

    with open(f'{csv_file.stem}.pickle', 'wb') as picklefile:
        pickle.dump(pickle_list, picklefile)


if __name__ == '__main__':
    csv_to_pickle(Path('users.csv'))