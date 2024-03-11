# Задание №3
# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import csv
import json
from pathlib import Path

__all__ = ['json_to_csv']


def json_to_csv(file: Path) -> None:
    """
    Преобразует данные из JSON-файла в файл CSV.

    Аргументы:
    file (Path): Путь к JSON-файлу, содержащему данные.

    Возвращает:
    None: Функция не возвращает значения, она просто записывает данные в файл CSV.

    Пример использования:
    >>> json_to_csv(Path('users.json'))
    """

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    rows = []
    for level, dict_level in data.items():
        for user_id, name in dict_level.items():
            rows.append({'level': int(level), 'id': int(user_id), 'name': name})

    with open(f'{file.stem}.csv', 'w', encoding='utf-8', newline='') as f:
        csv_write = csv.DictWriter(f, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    json_to_csv(Path('users.json'))