# Задание №1
# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдоименами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
from pathlib import Path

__all__ = ['convert_to_json']


def convert_to_json(input_file: Path) -> None:
    """
    Конвертирует данные из файла в формате "имя количество" в формат JSON.

    Аргументы:
    input_file (Path): Путь к входному файлу, содержащему данные.

    Возвращает:
    None: Функция ничего не возвращает.
    """

    data = {}

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            name, number = line.strip().split()
            data[name.title()] = float(number)

    with open(input_file.stem + '.json', "w", encoding="utf-8") as file_ex:
        json.dump(data, file_ex, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    convert_to_json(Path('result.txt'))
