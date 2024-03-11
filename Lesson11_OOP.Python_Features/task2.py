# Задание №2
# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """
    Класс Archive представляет собой простой архив для хранения чисел и текстовых данных.

    Атрибуты:
    _instance (Archive or None): Статический атрибут, хранящий единственный экземпляр класса.
    num (int): Число для хранения.
    text (str): Текст для хранения.
    list_num (list[int]): Список всех чисел, добавленных в архив.
    list_text (list[str]): Список всех текстовых данных, добавленных в архив.

    Методы:
    __init__(self, num: int, text: str): Инициализирует экземпляр класса с указанным числом и текстом.
    __new__(cls, *args, **kwargs): Создает новый экземпляр класса или возвращает существующий, если он уже существует.
    """
    _instance = None

    def __init__(self, num: int, text: str):
        """
        Инициализирует экземпляр класса с указанным числом и текстом.

        Аргументы:
        num (int): Число для хранения.
        text (str): Текст для хранения.

        Возвращает:
        None: Функция ничего не возвращает.
        """
        self.num = num
        self.text = text

    def __new__(cls, *args, **kwargs) -> 'Archive':
        """
        Создает новый экземпляр класса или возвращает существующий, если он уже существует.

        Аргументы:
        *args: Позиционные аргументы.
        **kwargs: Именованные аргументы.

        Возвращает:
        Archive: Новый или существующий экземпляр класса Archive.
        """
        print(args)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_num = []
            cls._instance.list_text = []
        else:
            cls._instance.list_num.append(cls._instance.num)
            cls._instance.list_text.append(cls._instance.text)

        return cls._instance

    def __repr__(self):
        return f'Archive: ({self.num},"{self.text}")'

    def __str__(self):
        return f'Архив из числа {self.num} и строки {self.text}, а также пара списков {self.list_num}, {self.list_text}'


archive = Archive(1, 'One')
archive_2 = Archive(2, 'Two')
archive_3 = Archive(3, 'Three')
archive_4 = Archive(4, 'Four')
print(archive.list_num)
print(archive.list_text)
print(archive)
print(repr(archive))
