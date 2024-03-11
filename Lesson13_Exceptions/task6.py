# Задание №6.
# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

import json
from pathlib import Path


class UserException(Exception):
    pass


class LevelError(UserException):
    def __init__(self, level, user):
        self.level = level
        self.user = user

    def __str__(self):
        return f"Не возможно добавить пользователя с уровнем '{self.level}'" \
               f" Пользователь '{self.user.name}' ограничен уровнем доступа '{self.user.level}'"


class AccessError(UserException):
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return (f'Вам отказано в доступе. Пользователя '
                f' с именем "{self.name}" и id={self.user_id} не существует.')


class User:
    def __init__(self, name, user_id, level):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'{self.name=}, {self.user_id=}, {self.level=}'

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self):
        return hash((str(self.name), str(self.user_id)))


class Repo:
    def __init__(self):
        self.user = None
        self.users = set()

    def read_file(self, file: Path) -> set[User]:
        with open(file, 'r', encoding='utf-8') as f:
            read_json = json.load(f)

        for level, value_dict in read_json.items():
            for user_id, user_name in value_dict.items():
                self.users.add(User(user_name, int(user_id), int(level)))

        return self.users

    def enter_user(self, name, user_id):
        current_user = User(name, user_id, 0)
        if current_user not in self.users:
            raise AccessError(name, user_id)

        for user in self.users:
            if user == current_user:
                self.user = user
                return self.user

    def add_user(self, name, user_id, level):
        if level < self.user.level:
            raise LevelError(level, self.user)
        new_user = User(name, user_id, level)
        self.users.add(new_user)
        return new_user


if __name__ == '__main__':
    repo = Repo()
    repo.read_file(Path(r'C:\Users\slavu\PycharmProjects\Dive_Into_Python\Lesson8_Serialization\users.json'))
    print(repo.enter_user('dob', 5))
    print(repo.add_user('seano', 8, 7))
    print(*repo.users, sep='\n')
