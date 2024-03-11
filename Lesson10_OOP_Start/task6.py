# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color


class Bird(Animal):
    def __init__(self, name, weight, wingspan, color):
        super().__init__(name, weight, color)
        self.wingspan = wingspan

    def get_wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name, weight, color, max_depth):
        super().__init__(name, weight, color)
        self.max_depth = max_depth

    def get_depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Обычная рыба'


class Mammal(Animal):
    def __init__(self, name, weight, height, color):
        super().__init__(name, weight, color)
        self.height = height

    def get_category(self):
        if self.height < 10:
            return 'Карликовый'
        elif self.height > 170:
            return 'Гигантский'
        return 'Обычный'


if __name__ == '__main__':
    pinguin = Bird('Kowalsky', 20, 60, 'Black-white')
    clown = Fish('Nemo', 1, 'Yellow', 88)
    zebra = Mammal('Martin', 150, 190, 'White')

    print(f'{pinguin.get_wing_length() = }')
    print(f'{clown.get_depth() = }')
    print(f'{zebra.get_category() = }')
