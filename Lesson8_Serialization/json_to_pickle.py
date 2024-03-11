# Задание №5
# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.

import json
import pickle
from pathlib import Path

__all__ = ['json_to_pickle']


def json_to_pickle(path: Path) -> None:
    """
    Преобразует JSON-файлы в файлы формата pickle.

    Аргументы:
    path (Path): Путь к директории, содержащей JSON-файлы.

    Возвращает:
    None: Функция ничего не возвращает.
    """
    for obj in path.iterdir():
        if obj.is_file() and obj.suffix == '.json':
            with open(obj, 'r', encoding='utf-8') as f_r:
                data = json.load(f_r)
            with open(f'{obj.stem}.pickle', 'wb') as f_w:
                pickle.dump(data, f_w)


if __name__ == '__main__':
    json_to_pickle(Path.cwd())