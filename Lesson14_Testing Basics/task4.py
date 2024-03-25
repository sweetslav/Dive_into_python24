from string import ascii_letters
import pytest

def del_symbol(text: str) -> str:
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()

def test_original_str():
    assert del_symbol('hello world') == 'hello world'

def test_lower():
    assert del_symbol('Hello worlD') == 'hello world'

def test_punctuation():
    assert del_symbol('hello, world!') == 'hello world'

def test_lang():
    assert del_symbol('hello world привет') == 'hello world '

def test_all():
    assert del_symbol('Hello, Worldпривет!!!') == 'hello world'

if __name__ == '__main__':
    pytest.main([__file__])
