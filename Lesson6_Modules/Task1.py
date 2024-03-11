# Задание №2
# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint

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
    print(guess())