# Задание №4
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import csv
import json
from pathlib import Path

__all__ = ['csv_to_json']


def csv_to_json(input_file: Path, output_file: Path) -> None:
    """
    Преобразует данные из CSV-файла в формат JSON.

    Аргументы:
    input_file (Path): Путь к входному CSV-файлу.
    output_file (Path): Путь к выходному JSON-файлу.

    Возвращает:
    None: Функция ничего не возвращает.
    """
    output_data = []
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_file:
        csv_read = csv.reader(csv_file, dialect='excel-tab')
        for nn, line in enumerate(csv_read):
            json_dict = {}
            if nn:  # Пропускаем первую строку (заголовки)
                level, user_id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f'{int(user_id):010}'
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
                output_data.append(json_dict)
    with open(output_file, 'w', encoding='utf-8') as fl:
        json.dump(output_data, fl, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('users.json'))