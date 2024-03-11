# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Bird:
    def __init__(self, name, weight, wingspan, color):
        self.name = name
        self.weight = weight
        self.wingspan = wingspan
        self.color = color

    def get_wing_length(self):
        return self.wingspan / 2

class Fish:
    def __init__(self, name, weight, color, max_depth):
        self.name = name
        self.weight = weight
        self.color = color
        self.max_depth = max_depth

    def get_depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Обычная рыба'

class Mammal:
    def __init__(self, name, weight, height, color):
        self.name = name
        self.weight = weight
        self.height = height
        self.color = color

    def get_category(self):
        if self.height < 10:
            return 'Карликовый'
        elif self.height > 280:
            return 'Гигантский'
        return 'Обычный'

if __name__ == '__main__':
    pinguin = Bird('Kowalsky', 20, 60 , 'Black-white')
    clown = Fish('Nemo', 1, 'Yellow', 88)
    zebra = Mammal('Martin', 150, 190, 'White')
    print(pinguin.get_wing_length())
    print(clown.get_depth())
    print(zebra.get_category())

