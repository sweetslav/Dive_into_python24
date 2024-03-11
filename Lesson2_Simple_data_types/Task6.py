# Задание №6
# напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import decimal

CMD_EXIT = 'в'
CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
NUMBER_OPERATION = 3
MULTIPLIER = 50
PERCENTAGE_WITHDRAW = decimal.Decimal(15) / decimal.Decimal(1000)
PERCENTAGE_RICHNESS = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUMM = decimal.Decimal(5_000_000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENTAGE_BONUS = decimal.Decimal(3) / decimal.Decimal(100)

balance = decimal.Decimal(1_000_000)
count = 0

while True:
    action = input(f'Ваш баланс: {balance:.2f} у.е.\n\n'
                   f'ПОПОЛНИТЬ - "{CMD_DEPOSIT}"\tСНЯТЬ - "{CMD_WITHDRAW}"\tВЫЙТИ - "{CMD_EXIT}"\n')
    if action == CMD_EXIT:
        print(f'Возьмите вашу карту. Ваш баланс: {balance:.2f} у.е.')
        break

    if action in (CMD_WITHDRAW, CMD_DEPOSIT):
        if balance > RICHNESS_SUMM:
            percent = balance * PERCENTAGE_RICHNESS
            balance -= percent
            print(f"С вашего баланса был удержан налог на богатство {PERCENTAGE_RICHNESS * 100}% "
                  f"в размере {percent:.2f} у.е. Ваш баланс составляет {balance:.2f} у.е.")

        amount = 1
        while amount % MULTIPLIER != 0:
            amount = decimal.Decimal(input(f'Введите сумму: (должна быть кратна {MULTIPLIER}): '))

        if action == CMD_DEPOSIT:
            count += 1
            balance += amount
            print(f'Пополнение на {amount:.2f} у.е. Ваш баланс: {balance:.2f} у.е.')

        elif action == CMD_WITHDRAW:
            percent = amount * PERCENTAGE_WITHDRAW
            percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
            sub = amount + percent
            if balance > sub:
                balance -= sub
                count += 1
                print(f'Снятие {amount:.2f} у.е. Комиссия {percent:.2f}. Ваш баланс: {balance:.2f} у.е.')
            else:
                print(f'Недостаточно средств на карте. Ваш баланс: {balance:.2f} у.е.')

    if count % NUMBER_OPERATION == 0:
        bonus = balance * PERCENTAGE_BONUS
        balance += bonus
        print(f'Начислен бонус {bonus:.2f} за каждую {NUMBER_OPERATION} операцию. Ваш баланс равен {balance:.2f} у.е.')
