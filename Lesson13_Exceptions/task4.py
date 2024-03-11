# Задание №4.
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.


import json
from pathlib import Path


class User:
    def __init__(self, user_id, level, name):
        self.user_id = user_id
        self.level = level
        self.name = name

    def __str__(self):
        return f'{self.user_id=} - {self.level=} - {self.name=}'


def read_json_file(file: Path) -> set[User]:
    with open(file, 'r', encoding='utf-8') as f:
        read_json = json.load(f)

        users = set()

        for level, values in read_json.items():
            for user_id, user_name in values.items():
                users.add(User(user_id=user_id, name=user_name, level=level))

        return users


if __name__ == '__main__':
    print(*read_json_file(Path(r'C:\Users\slavu\PycharmProjects\Dive_Into_Python\Lesson8_Serialization\users.json')),
          sep='\n')
