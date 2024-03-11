# Задание №5.
# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# 1) загрузка данных (функция из задания 4)
# 2) вход в систему - требует указать имя и id пользователя.
#       Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
#       Если такого пользователя нет, вызывайте исключение доступа.
#       А если пользователь есть, получите его уровень из множества пользователей.
# 3) добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.


import json
from pathlib import Path


class UserException(Exception):
    pass


class LevelError(UserException):
    pass


class AccessError(UserException):
    pass


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
            raise AccessError('ACCESS DENIED')

        for user in self.users:
            if user == current_user:
                self.user = user
                return self.user

    def add_user(self, name, user_id, level):
        if level < self.user.level:
            raise LevelError('INVALID LEVEL')
        new_user = User(name, user_id, level)
        self.users.add(new_user)
        return new_user


if __name__ == '__main__':
    repo = Repo()
    repo.read_file(Path(r'C:\Users\slavu\PycharmProjects\Dive_Into_Python\Lesson8_Serialization\users.json'))
    print(repo.enter_user('dob', 5))
    print(repo.add_user('Shilo', 8, 7))
    print(*repo.users, sep='\n')