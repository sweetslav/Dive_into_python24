# Задание №3
# � Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# � Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

__all__=['guess'















         ]

from random import randint
from sys import argv

def guess(low_limit: int=0, high_limit: int=100, count: int=10) -> bool:
    number = randint(low_limit, high_limit)
    for _ in range(count):
        answer = int(input("Enter a number: "))
        if answer == number:
            print("Congratulations! You guessed")
            return True
        elif answer < number:
            print("Too low")
        elif answer > number:
            print("Too high")
    return False

if __name__ == '__main__':
    params = (argv[1:])
    params = (int(num) for num in params)
    print(guess(*params))