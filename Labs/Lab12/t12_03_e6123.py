class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
        return "ok"

    def pop(self):
        if not self._items:
            return "error"
        item = self._items[-1]
        self._items.pop()
        return item

    def back(self):
        if not self._items:
            return "error"
        return self._items[-1]

    def size(self):
        return len(self._items)

    def clear(self):
        self._items.clear()
        return "ok"

    def exit(self):
        print("bye")
        exit()

    def execute(self, command: str):
        method, *args = command.split()
        return getattr(self, method)(*args)

if __name__ == "__main__":
    stack = Stack()
    while True:
        try:
            command = input()
            print(stack.execute(command))
        except EOFError:
            break