import sys


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node' | None = None


class List:
    def __init__(self):
        self.head: 'Node' | None = None
        self.tail: 'Node' | None = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв'язного Списку"""
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self) -> None:
        """Вивести елементи Зв'язного Списку"""
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def PrintReverse(self) -> None:
        """Вивести елементи Зв'язного Списку в зворотному порядку"""
        self._print_reverse_recursive(self.head)
        print()

    def _print_reverse_recursive(self, node: 'Node' | None) -> None:
        """Допоміжний рекурсивний метод для зворотного виводу без масивів"""
        if node is None:
            return

        self._print_reverse_recursive(node.next)
        print(node.data, end=" ")

if __name__ == "__main__":
    input_data = sys.stdin.read().split()

    if input_data:
        n = int(input_data[0])
        my_list = List()

        for i in range(1, n + 1):
            my_list.addToTail(int(input_data[i]))

        my_list.Print()
        my_list.PrintReverse()