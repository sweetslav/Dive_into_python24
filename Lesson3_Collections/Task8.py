# Задание №8
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

hike = {
    'Aaz': ("спички", "спальник", "дрова", "топор"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "спички", "косметичка"),
}

all_things = set()

# all_things.update(*hike.values())

for value in hike.values():
    all_things.update(value)

print(f'Full list of {all_things = }')

unique = {}

for master_friend, master_things in hike.items():
    for slave_friend, slave_things in hike.items():
        if master_friend != slave_friend:
            if master_friend not in unique:
                unique[master_friend] = set(master_things) - set(slave_things)
            else:
                unique[master_friend] -= set(slave_things)
print(f'Unique things {unique = }')

duplicates = set(all_things)

# uniq_things = set()
# uniq_things.update(*unique.values())
# print(uniq_things)
# duplicates -= set(unique.values())
# print(duplicates)

for things in unique.values():
    duplicates -= things
print(f'Duplicate things {duplicates = }')

for friend, things in hike.items():
    no_things = duplicates - set(things)
    if no_things:
        print(f'Friend {friend} have no {no_things}')