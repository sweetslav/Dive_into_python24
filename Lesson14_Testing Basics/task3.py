# Задание №3
# Напишите для задачи 1 тесты unittest.
# Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest
from string import ascii_letters


def del_symbol(text: str) -> str:
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()


class TestCaseName(unittest.TestCase):
    def test_original_string(self):
        self.assertEqual('hello world', del_symbol('hello world'), 'String did not change')

    def test_lower(self):
        self.assertEqual('hello world', del_symbol('Hello World'), 'Case is not lower')

    def test_punctuation(self):
        self.assertEqual('hello world', del_symbol('hello world,&!'), 'Text with punctuation did not change')

    def test_language(self):
        self.assertEqual('hello world', del_symbol('hello worldприветмир'), 'Russian text did not change')

    def test_all(self):
        self.assertEqual('hello world', del_symbol('heLLo World!приветмир'), 'All text did not change')


if __name__ == '__main__':
    unittest.main(verbosity=2)
