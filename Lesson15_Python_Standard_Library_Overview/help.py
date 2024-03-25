FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" в строке {lineno:03d} функция "{funcName}()" в {created} секунд записала сообщение: {msg}'

basicConfig(
    filename='project.log',     # filename='project.log' - имя файла логирования
    filemode='w',               # filemode='w'           - режим записи - 'w' или 'a'
    encoding='utf-8',           # encoding='utf-8'       - кодировка
    level=NOTSET,               # level=NOTSET           - уровень логирования
    format=FORMAT,              # format=FORMAT          - формат строки для логирования
    style='{')                  # style='{'              стиль для строки форматирования

                                # errors - как обрабатывать ошибки, если возникают проблемы с кодировкой.

# Уровни логирования:
NOTSET, 0 # - без уровня, регистрируются все события
DEBUG, 10 # - подробная информация, для дебагинга
INFO, 20 # - подтверждение, что всё хорошо работает
WARNING, 30 # - что-то не так, или будет не так ...
ERROR, 40 # - программа не может что-то выполнить
CRITICAL, 50 # - программа не может дальше работать