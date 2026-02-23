"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

size: int
keys: list[str]  # імена авторів
values: list[str]  # назви книг
count: int

EMPTY = "EMPTY"
DELETED = "DELETED"


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global size, keys, values, count
    size = 11
    keys = [EMPTY] * size
    values = [EMPTY] * size
    count = 0


def _hash(author: str, current_size: int) -> int:
    """ Допоміжна функція для обчислення хешу рядка. """
    h = 516
    for char in author:
        h = ((h << 3) + h) + ord(char)
    return h % current_size


def _rehash():
    """ Допоміжна функція для збільшення розміру таблиці. """
    global size, keys, values, count
    old_keys = keys
    old_values = values

    size = size * 2
    keys = [EMPTY] * size
    values = [EMPTY] * size
    count = 0

    for k, v in zip(old_keys, old_values):
        if k != EMPTY and k != DELETED:
            addBook(k, v)


def addBook(author: str, title: str):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global size, keys, values, count

    if count >= size * 0.7:
        _rehash()

    if find(author, title):
        return

    idx = _hash(author, size)
    i = 0
    insert_idx = -1

    while keys[(idx + i) % size] != EMPTY:
        current_idx = (idx + i) % size
        if keys[current_idx] == DELETED and insert_idx == -1:
            insert_idx = current_idx
        i += 1

    if insert_idx == -1:
        insert_idx = (idx + i) % size

    keys[insert_idx] = author
    values[insert_idx] = title
    count += 1


def find(author: str, title: str) -> bool:
    """ Перевіряє чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    global size, keys, values
    if count == 0:
        return False

    idx = _hash(author, size)
    i = 0

    while keys[(idx + i) % size] != EMPTY:
        current_idx = (idx + i) % size
        if keys[current_idx] == author and values[current_idx] == title:
            return True
        i += 1
        if i == size:
            break
    return False


def delete(author: str, title: str):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global size, keys, values, count
    if count == 0:
        return

    idx = _hash(author, size)
    i = 0

    while keys[(idx + i) % size] != EMPTY:
        current_idx = (idx + i) % size
        if keys[current_idx] == author and values[current_idx] == title:
            keys[current_idx] = DELETED
            values[current_idx] = DELETED
            count -= 1
            return
        i += 1
        if i == size:
            break


def findByAuthor(author: str) -> list[str]:
    """ Повертає список книг заданого автора.
    Якщо бібліотека не містить книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    global size, keys, values
    result = []
    if count == 0:
        return result

    idx = _hash(author, size)
    i = 0

    while keys[(idx + i) % size] != EMPTY:
        current_idx = (idx + i) % size
        if keys[current_idx] == author:
            result.append(values[current_idx])
        i += 1
        if i == size:
            break
    return sorted(result)