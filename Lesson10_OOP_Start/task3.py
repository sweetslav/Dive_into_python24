# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы:
# birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

class Human:
    def __init__(self, fio, age):
        self.fio = fio
        self._age = age

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.fio = }'


if __name__ == '__main__':
    human_1 = Human('Sweetslav Krivosheev', 29)
    print(human_1.full_name())
    print(human_1.get_age())
    human_1.birthday()
    print(human_1.get_age())
    human_1.age = 50
    print(human_1.get_age())
