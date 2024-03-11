# Задание №6
# � Добавьте в модуль с загадками функцию,# которая принимает на вход строку (текст) и число (номер).
# � Функция формирует словарь с информацией о результатах отгадывания.
# � Для хранения используйте защищённый словарь уровня модуля.
# � Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# � Для формирования результатов используйте генераторное выражение.

__all__=['save','secrets','storage','show']

_data = {}


def save(puzzle: str, count: int) -> None:
    _data.update({puzzle: count})


def secrets(puzzle: str, answers: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку: {puzzle}')
    for i in range(1, count + 1):
        answer = input(f'Попытка №{i}, Твой ответ: ')
        if answer in answers:
            return i
    return 0


def storage():
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
    res = (f'Загадку {puzzle} угадали с {count}-й попытки' if count
           else f'Загадку {puzzle} не угадали.'
           for puzzle, count in _data.items()
           )
    print(*res, sep='\n')


if __name__ == '__main__':
    storage()
    print()
    show()
