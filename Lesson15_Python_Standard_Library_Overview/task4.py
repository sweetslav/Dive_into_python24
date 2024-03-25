# Задание №4.
# Функция получает на вход текст вида: “1-й четверг ноября”, “3- я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответствует формату.


import logging
from datetime import datetime as dt

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='info4.log', level=logging.INFO, encoding='utf-8', filemode='a', style='%')
logger = logging.getLogger(__name__)

MONTHS = ['', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек', ]
DAYS = ['пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос', ]


def get_date(date: str):
    try:
        count, day, month = date.split()
        count = int(count[0])
        day = DAYS.index(day[:3])
        month = MONTHS.index(month[:3])
    except ValueError as e:
        logger.error(f'Не удалось разобрать строку "{date}": "{e}"')
        return None

    now = dt.now()
    for d in range(1, 32):
        temp_date = dt(day=d, month=month, year=now.year)
        if temp_date.weekday() == day:
            count -= 1
            if count == 0:
                return temp_date.strftime('%d.%m.%Y')

    logger.error(f'Не удалось найти дату для {date}')
    return None


if __name__ == '__main__':
    print(get_date('4-й понедельник марта'))
    print(get_date('1-евоскресеньедекабря'))

