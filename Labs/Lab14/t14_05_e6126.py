import sys

class Node:
    def __init__(self, item):
        self._item = item
        self._next = None

class Queue:
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
        else:
            self._back._next = node

        self._back = node
        self._size += 1

        return "ok"

    def pop(self):
        if self._size == 0:
            return "error"

        item = self._front._item
        self._front = self._front._next
        self._size -= 1

        if self._size == 0:
            self._back = None

        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._front._item

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
    queue = Queue()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        result = queue.execute(line)

        if result is not None:
            print(result)

        if result == "bye":
            break