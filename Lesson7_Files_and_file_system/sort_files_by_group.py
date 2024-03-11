# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from os import chdir
from pathlib import Path

__all__ = ['sort_files_by_group']


def sort_files_by_group(path: Path) -> None:
    """
    Сортирует файлы в указанной директории по заданным группам.

    Аргументы:
    path (Path): Путь к директории, содержащей файлы для сортировки.

    Возвращает:
    None: Функция ничего не возвращает.
    """
    chdir(path)

    # Define groups dictionary
    groups = {
        Path('Videos'): ['mp4', 'mov', 'mkv'],
        Path('Documents'): ['txt', 'doc', 'pdf'],
        Path('Data'): ['pickle', 'json', 'csv'],
        Path('Images'): ['jpg', 'jpeg', 'png']
    }

    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir(parents=True)

    for file in path.iterdir():
        if file.is_file():
            for target_dir, ext_list in groups.items():
                for ext in ext_list:
                    if file.suffix == f'.{ext}':
                        target_file = target_dir / file.name
                        if not target_file.exists():
                            file.replace(target_file)
                        else:
                            print(f"File '{file.name}' already exists in '{target_dir}', skipping...")
                        break


if __name__ == '__main__':
    sort_files_by_group(Path(r'C:\Users\slavu\PycharmProjects\Dive_Into_Python\Lesson7'))


