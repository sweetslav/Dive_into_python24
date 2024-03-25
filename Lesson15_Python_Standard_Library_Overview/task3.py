# Задание №3.
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging
from typing import Callable

FORMAT = '{levelname:<8} - {asctime}. {message}'

logging.basicConfig(filename='info.log.', filemode='a', style='{', encoding='utf-8', level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


def my_logger(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        info_dict = {'args': args, **kwargs, 'result': result}
        logger.info(f'Функция - {func.__name__}(), аргументы: {info_dict}, результат: {result}')
        return result

    return wrapper


@my_logger
def get_all(num1: int, *args, **kwargs) -> int:
    return num1


if __name__ == '__main__':
    print(get_all(1, 2, 3, 4, 5, 'sadsdsd', pupa='lupa'))