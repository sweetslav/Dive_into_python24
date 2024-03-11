# Задание №3.
# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class UserException(Exception):
    pass


class LevelError(UserException):
    pass


class AccessError(UserException):
    pass
