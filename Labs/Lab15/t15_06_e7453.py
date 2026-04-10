import sys

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node' | None = None

class List:
    def __init__(self):
        self.head: 'Node' | None = None
        self.tail: 'Node' | None = None
        self._length: int = 0

    def AddToTail(self, val: int) -> None:
        """Додати число val у кінець зв'язаного списку"""
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._length += 1

    def RotateRight(self, k: int) -> None:
        """Обернути список праворуч на k позицій"""
        if self._length <= 1:
            return

        k = k % self._length
        if k == 0:
            return

        self.tail.next = self.head

        steps_to_new_tail = self._length - k
        new_tail = self.head

        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        self.head = new_tail.next
        new_tail.next = None
        self.tail = new_tail

    def Print(self) -> None:
        """Вивести елементи зв'язаного списку"""
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    input_data = sys.stdin.read().split()

    if input_data:
        n = int(input_data[0])
        my_list = List()

        for i in range(1, n + 1):
            my_list.AddToTail(int(input_data[i]))

        for i in range(n + 1, len(input_data)):
            k = int(input_data[i])
            my_list.RotateRight(k)
            my_list.Print()