# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

from string import ascii_letters
print(ascii_letters)

def del_symbol(text: str) -> str:
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()

if __name__ == '__main__':
    text = 'Hello Привет World мир'
    print(del_symbol(text))


