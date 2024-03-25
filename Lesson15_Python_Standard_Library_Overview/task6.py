# Задание №6.
# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.


import argparse
from pathlib import Path
import logging
from collections import namedtuple

logging.basicConfig(filename='fileinfo.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', 'name, extension, dir, parent')


def read_dir(path: Path) -> None:
    for file in path.iterdir():
        # print(f'{file.stem if file.is_file() else file.name = }')
        # print(f'{file.suffix = }')
        # print(f'{file.is_dir() = }')
        # print(f'{file.parent = }')
        obj = File(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(obj)
        if obj.dir:
            read_dir(Path(obj.parent) / obj.name)

def walker():
    parser = argparse.ArgumentParser(
        description='Сохраняем данные о каталоге в файл',
        prog='read_dir()')
    parser.add_argument('-p', '--path', type=Path, required=True, help='Введите путь: ')
    args = parser.parse_args()
    return read_dir(args.path)


if __name__ == '__main__':
    walker()