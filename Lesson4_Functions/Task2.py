# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

def print_unicode_list(text: str):
    text = [ord(c) for c in set(text)]
    return sorted(text, reverse=True)

print(print_unicode_list(input()), sep='\n')