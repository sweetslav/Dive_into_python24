# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных, оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце

def remove_s() -> None:
    dict_vars = globals()
    for key in dict_vars.copy():
        if key.endswith('s') and key != 's':
            dict_vars[key[:-1]] = dict_vars[key]
            dict_vars[key] = None
    print(dict_vars)



datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

print(remove_s())
#print(*globals().items(), sep='\n')
print(f'{names = }')
print(f'{name = }')
