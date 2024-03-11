# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint


def guess_num(func):
    MAX_LIM = 100
    MIN_LIM = 1
    MAX_CNT = 10
    MIN_CNT = 1

    def wrapper(num: int, count: int):
        if num < MIN_LIM or num > MAX_LIM:
            num = randint(MIN_LIM, MAX_LIM)
        if count < MAX_CNT or count > MAX_CNT:
            count = randint(MIN_CNT, MAX_CNT)
        print(f'У вас {count} попыток')
        return func(num, count)

    return wrapper


@guess_num
def guess_game(num: int, count: int):
    for i in range(1, count + 1):
        print(f'Попытка номер {i}')
        user_input = int(input('Введите число от 1 до 100: '))
        if num == user_input:
            print(f'Вы угадали с {i} попытки')
            return
        elif num < user_input:
            print('Ваше число больше')
        elif num > user_input:
            print('Ваше число меньше')
    else:
        print(f'Было загадано число {num}')


if __name__ == '__main__':
    guess_game(250, 15)
