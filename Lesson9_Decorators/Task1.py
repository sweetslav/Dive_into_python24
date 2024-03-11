# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.


def guess_num(num: int, count: int):
    def guess_game():
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

    return guess_game


if __name__ == '__main__':
    game = guess_num(1, 100)
    game()
