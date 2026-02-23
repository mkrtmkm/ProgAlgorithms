"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
Хеш-таблиця з розв'язанням колізій методом ланцюжків.
"""

size: int
keys: list[list[str]]
values: list[list[str]]
count: int


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global size, keys, values, count
    size = 11
    keys = [[] for _ in range(size)]
    values = [[] for _ in range(size)]
    count = 0


def _hash(author: str, current_size: int) -> int:
    """ Допоміжна функція для обчислення хешу рядка. """
    h = 516
    for char in author:
        h = ((h << 3) + h) + ord(char)
    return h % current_size


def _rehash():
    """ Збільшення розміру таблиці. """
    global size, keys, values, count
    old_keys = keys
    old_values = values

    size = size * 2
    keys = [[] for _ in range(size)]
    values = [[] for _ in range(size)]
    count = 0

    for chain_keys, chain_values in zip(old_keys, old_values):
        for k, v in zip(chain_keys, chain_values):
            addBook(k, v)


def addBook(author: str, title: str):
    """ Додає книгу до бібліотеки. """
    global size, keys, values, count

    if count >= size * 0.7:
        _rehash()

    if find(author, title):
        return

    idx = _hash(author, size)
    keys[idx].append(author)
    values[idx].append(title)
    count += 1


def find(author: str, title: str) -> bool:
    """ Перевіряє чи міститься задана книга у бібліотеці. """
    global size, keys, values
    if count == 0:
        return False

    idx = _hash(author, size)

    for i in range(len(keys[idx])):
        if keys[idx][i] == author and values[idx][i] == title:
            return True

    return False


def delete(author: str, title: str):
    """ Видаляє книгу з бібліотеки. """
    global size, keys, values, count
    if count == 0:
        return

    idx = _hash(author, size)

    for i in range(len(keys[idx])):
        if keys[idx][i] == author and values[idx][i] == title:
            keys[idx].pop(i)
            values[idx].pop(i)
            count -= 1
            return


def findByAuthor(author: str) -> list[str]:
    """ Повертає список книг заданого автора. """
    global size, keys, values
    result = []
    if count == 0:
        return result

    idx = _hash(author, size)

    for i in range(len(keys[idx])):
        if keys[idx][i] == author:
            result.append(values[idx][i])
    return sorted(result)