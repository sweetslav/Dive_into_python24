# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.
import decimal


def func_dict(names: list[str], salaries: list[float], bonuses: list[str]) -> dict[str: decimal.Decimal]:
    result = {}
    for name, salary, bonus in zip(names, salaries, bonuses):
        result[name] = salary * decimal.Decimal(bonus.replace('%',''))
        #result[name] = salary * decimal.Decimal(bonus[:-1])

    return result

n = ["Иван", "Николай", "Пётр", "Харитон"]
s = [125_000, 96_000, 109_000, 100_000]
a = ['10%', '25.5%', '13.3%', '42.73%']

print(func_dict(n, s, a))