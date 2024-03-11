# Задание №6
# Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.

from random import randint as rnd
import json
from typing import Callable
from pathlib import Path
from functools import wraps

def save_to_json(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        file = Path(f'{func.__name__}.json')
        if file.is_file():
            with open(file, 'r', encoding='utf-8') as f_r:
                list_of_dicts = json.load(f_r)
        else:
            list_of_dicts = []

        result = func(*args, **kwargs)
        json_dict = {'args': args, **kwargs, 'result': result}
        list_of_dicts.append(json_dict)
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(list_of_dicts, f)
        return result

    return wrapper

def deco_count(num: int):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal num
            st = ''
            for count in range(1, num + 1):
                print(f'Запустили функцию {count} раз')
                res = func(*args, **kwargs)
                st += str(res)
            return st

        return wrapper

    return deco

def guess_num(func):
    MAX_LIM = 100
    MIN_LIM = 1
    MAX_CNT = 10
    MIN_CNT = 1

    @wraps(func)
    def wrapper(num: int, count: int):
        if num < MIN_LIM or num > MAX_LIM:
            num = rnd(MIN_LIM, MAX_LIM)
        if count < MIN_CNT or count > MAX_CNT:
            count = rnd(MIN_CNT, MAX_CNT)
        print(f'У вас {count} попыток')
        return func(num, count)

    return wrapper

@deco_count(5)
@guess_num
@save_to_json
def guess_game(num: int, count: int):
    for i in range(1, count + 1):
        print(f'Попытка {i}')
        while True:
            try:
                user_input = int(input('Введи число от 1 до 100: '))
                break
            except ValueError:
                print("Ошибка! Введите целое число.")

        if num == user_input:
            print(f'Вы угадали с {i} попытки.')
            return
        elif num < user_input:
            print('Ваше число больше')
        elif num > user_input:
            print('Ваше число меньше')
        else:
            print(f'Было загадано {num}')

if __name__ == '__main__':
    guess_game(250, 15)
