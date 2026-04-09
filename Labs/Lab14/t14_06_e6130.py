import sys

class Node:
    def __init__(self, item):
        self._item = item
        self._next = None
        self._prev = None


class Deque:
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push_front(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
            self._back = node
        else:
            node._next = self._front
            self._front._prev = node
            self._front = node

        self._size += 1
        return "ok"

    def push_back(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
            self._back = node
        else:
            node._prev = self._back
            self._back._next = node
            self._back = node

        self._size += 1
        return "ok"

    def pop_front(self):
        if self._size == 0:
            return "error"

        item = self._front._item
        self._front = self._front._next
        self._size -= 1

        if self._size == 0:
            self._back = None
        else:
            self._front._prev = None
        return item

    def pop_back(self):
        if self._size == 0:
            return "error"

        item = self._back._item
        self._back = self._back._prev
        self._size -= 1

        if self._size == 0:
            self._front = None
        else:
            self._back._next = None

        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._front._item

    def back(self):
        if self._size == 0:
            return "error"
        return self._back._item

    def size(self):
        return self._size

    def clear(self):
        self._front = None
        self._back = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    deque = Deque()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        result = deque.execute(line)

        if result is not None:
            print(result)

        if result == "bye":
            break