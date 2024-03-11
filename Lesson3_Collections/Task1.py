# Задание №1
# Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

print(*set(data))

new_list = []
for el in data:
    if el not in new_list:
        new_list.append(el)
print(*new_list)

new_sorted_list = sorted(data)

unique_list = []
prev_item = None

for item in data:
    if item != prev_item:
        unique_list.append(item)
        prev_item = item

print(unique_list)