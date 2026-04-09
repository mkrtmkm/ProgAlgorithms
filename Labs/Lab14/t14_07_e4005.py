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

    def pop(self):
        if self._size == 0:
            return None

        item = self._front._item
        self._front = self._front._next
        self._size -= 1

        if self._size == 0:
            self._back = None

        return item

    def is_empty(self):
        return self._size == 0


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    half = n // 2

    q1 = Queue()
    q2 = Queue()

    for i in range(1, half + 1):
        q1.push(int(input_data[i]))

    for i in range(half + 1, n + 1):
        q2.push(int(input_data[i]))

    moves = 0
    limit = 200000

    while not q1.is_empty() and not q2.is_empty() and moves < limit:
        moves += 1

        c1 = q1.pop()
        c2 = q2.pop()

        if c1 == 0 and c2 == n - 1:
            p1_wins = True
        elif c2 == 0 and c1 == n - 1:
            p1_wins = False
        else:
            p1_wins = c1 > c2

        if p1_wins:
            q1.push(c1)
            q1.push(c2)
        else:
            q2.push(c1)
            q2.push(c2)

    if q1.is_empty():
        print(f"second {moves}")
    elif q2.is_empty():
        print(f"first {moves}")
    else:
        print("draw")


if __name__ == '__main__':
    solve()