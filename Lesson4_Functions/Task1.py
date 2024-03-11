# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.


def print_string(text):
    text = sorted(text.split())
    max_len_word = len(max(text, key=len))

    for nn, word in enumerate(text, 1):
        #print(f'{nn}. {word:>{max_len_word}}')
        print(f'{nn}. {word.rjust(max_len_word)}')

input_string = input('Enter a string: ')
print(print_string(input_string))