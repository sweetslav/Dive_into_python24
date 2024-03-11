# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = 255

# Введите ваше решение ниже

hex_list = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
result = ''
original_num = num

while num:
    cur_dig = num % 16
    if cur_dig in hex_list:
        cur_dig = hex_list[cur_dig]
    result = str(cur_dig) + result
    num = num // 16

print(f'Шестнадцатеричное представление числа: {result}')
print(f'Проверка результата: {hex(original_num)}')
