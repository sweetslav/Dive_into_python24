# Задание №7
# � Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную защищённую функцию.

__all__=['is_valid_date','is_leap_year']

def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def is_valid_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))

    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False

    elif month in (4, 6, 9, 11):
        return day < 31

    elif month == 2:
        if is_leap_year(year):
            return day < 30
        else:
            return day < 29
    else:
        return True


if __name__ == '__main__':
    date_to_prov = '10.04.2023'
    date_to_prov1 = '32.1.2023'
    date_to_prov2 = '15.0.2023'
    date_to_prov3 = '15.14.2023'
    date_to_prov4 = '-15.04.2023'
    date_to_prov5 = '15.-02.2020'
    date_to_prov6 = '-31.02.-2023'
    date_to_prov7 = '31.02.2023'
    date_to_prov8 = '-31.02.2100'
    print(is_valid_date(date_to_prov))
    print(is_valid_date(date_to_prov1))
    print(is_valid_date(date_to_prov2))
    print(is_valid_date(date_to_prov3))
    print(is_valid_date(date_to_prov4))
    print(is_valid_date(date_to_prov5))
    print(is_valid_date(date_to_prov6))
    print(is_valid_date(date_to_prov7))
    print(is_valid_date(date_to_prov8))
