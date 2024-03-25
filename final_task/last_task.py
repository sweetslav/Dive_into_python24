# Задание
# Решить задачи, которые не успели решить на семинаре.
# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import logging
import argparse
import sys


logging.basicConfig(
    filename='puzzle.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


_data = {}


def save(puzzle: str, count: int) -> None:
    """Сохраняет результат угадывания загадки."""
    _data.update({puzzle: count})


def secrets(puzzle: str, answers: list[str], count: int = 3) -> int:
    """Задает загадку и позволяет пользователю попытаться угадать ответ."""
    logger.info(f'Отгадывается загадка: {puzzle}')
    print(f'Отгадай загадку: {puzzle}')  # Добавлен вывод текста загадки
    for i in range(1, count + 1):
        try:
            answer = input(f'Попытка №{i}, Ваш ответ: ')
        except KeyboardInterrupt:
            print("\nВыход из программы...")
            sys.exit(0)
        if answer in answers:
            logger.info(f'Пользователь угадал загадку {puzzle} с {i}-й попытки.')
            return i
    logger.info(f'Пользователь не угадал загадку {puzzle}.')
    return 0


def storage():
    """Хранилище загадок и их угадывание."""
    puzzles = {
        'Зимой и летом одним цветом': ['ёлка', 'доллар', 'сосна', 'елка', ],
        'Висит груша - нельзя скушать': ['лук', 'лампочка', 'люстра', 'луна', ],
        'Сидит дед в сто шуб одет': ['капуста', 'лук', 'луковица', 'елка', ],
        'Не лает не кусает, в дом не пускает': ['пес', 'замок', 'дед', 'домофон', ],
    }
    for key, value in puzzles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки' if result else 'Не угадал')
        save(key, result)


def show():
    """Показывает результаты угадывания загадок."""
    res = (f'Загадку {puzzle} угадали с {count}-й попытки' if count
           else f'Загадку {puzzle} не угадали.'
           for puzzle, count in _data.items()
           )
    print(*res, sep='\n')


def main():
    """Главная функция для запуска скрипта из командной строки."""
    parser = argparse.ArgumentParser(description='Угадайте загадки!')
    parser.add_argument('-s', '--storage', action='store_true', help='Запустить хранилище загадок')
    parser.add_argument('-sh', '--show', action='store_true', help='Показать результаты угадывания загадок')
    args = parser.parse_args()

    if args.storage:
        storage()
    elif args.show:
        show()
    else:
        print('Используйте -s или -sh для запуска соответствующей функции.')


if __name__ == '__main__':
    main()
