# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

class MyString(str):
    """
    Пользовательский класс строк, производный от встроенного типа `str`.

    Добавляет к строке дополнительные атрибуты `name` и `time` при создании экземпляра.

    Атрибуты:
    name (str): Имя экземпляра.
    time (float): Время создания экземпляра (в секундах с начала эпохи).

    Методы:
    __new__(cls, name: str, value: str) -> MyString: Создает новый экземпляр класса.
    """

    def __new__(cls, name: str, value: str) -> 'MyString':
        """
        Создает новый экземпляр класса MyString с заданными именем и значением.

        Аргументы:
        name (str): Имя, связанное с экземпляром.
        value (str): Значение строки.

        Возвращает:
        MyString: Новый экземпляр класса MyString.
        """
        import time
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        print(f'Create class {cls}. {instance.name = }, {instance.time =}')

        return instance


# Пример использования
mystring = MyString('Steeve', 'Hello world')
