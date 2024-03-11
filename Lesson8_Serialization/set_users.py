# Задание №2
# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключом для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
from pathlib import Path

__all__ = ['set_users']


def set_users(user_file: Path) -> None:
    """
    Запрашивает у пользователя имя, идентификатор и уровень доступа, добавляя их в JSON-файл.

    Аргументы:
    user_file (Path): Путь к JSON-файлу, в который записывается информация о пользователях.

    Возвращает:
    None: Функция ничего не возвращает.
    """

    unique_id = set()

    if not user_file.is_file():
        data = {str(i): {} for i in range(1, 7 + 1)}
    else:
        with open(user_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for dict_level in data.values():
                unique_id.update(dict_level.keys())

    while True:
        name = input('Enter a name: ')
        if not name:
            break
        user_id = input('Enter an id: ')
        user_level = input('Enter a level from 1 to 7: ')
        while user_level not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Incorrect input. Try again.')
            user_level = input('Enter a level from 1 to 7: ')

        if user_id not in unique_id:
            data[user_level][user_id] = name
            unique_id.add(user_id)

        with open(user_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    set_users(Path('users.json'))

