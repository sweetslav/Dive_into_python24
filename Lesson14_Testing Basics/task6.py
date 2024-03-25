# Задание №6
# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры
@pytest.fixture
def new_set():
    data = {
        User('Petr', 1, 1),
        User('Ivan', 2, 3),
        User('Petr', 3, 3),
        User('Maria', 5, 5)
    }

    return data


@pytest.fixture
def new_user():
    return User('Bill', 456, 5)


@pytest.fixture
def good_user():
    return User('Ivan', 2, 3)


def test_load(new_set):
    project = Repo()
    result = project.read_file(Path(r'C:\Users\permk\PycharmProjects\pythonGB\seminar_8\users.json'))
    assert result == new_set


def test_enter(good_user):
    project = Repo()
    project.read_file(Path(r'C:\Users\permk\PycharmProjects\pythonGB\seminar_8\users.json'))
    result = project.enter_user('Ivan', 2)
    assert result == good_user


def test_no_enter():
    project = Repo()
    project.read_file(Path(r'C:\Users\permk\PycharmProjects\pythonGB\seminar_8\users.json'))
    with pytest.raises(AccessError):
        project.enter_user('TTTT', 2)


def test_add_user(new_user):
    project = Repo()
    project.read_file(Path(r'C:\Users\permk\PycharmProjects\pythonGB\seminar_8\users.json'))
    project.enter_user('Ivan', 2)
    result = project.add_user('Bill', 456, 5)
    assert result == new_user


def test_not_add_user(new_user):
    project = Repo()
    project.read_file(Path(r'C:\Users\permk\PycharmProjects\pythonGB\seminar_8\users.json'))
    project.enter_user('Ivan', 2)
    with pytest.raises(LevelError):
        project.add_user('Bill', 456, 1)
