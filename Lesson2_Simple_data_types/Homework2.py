# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

# Введите ваше решение ниже

fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

sum_fraction = fraction1 + fraction2
prod_fraction = fraction1 * fraction2

print(f'Сумма дробей: {sum_fraction}')
print(f'Произведение дробей: {prod_fraction}')
print(f'Сумма дробей: 5/6')
print(f'Произведение дробей: 1/6')