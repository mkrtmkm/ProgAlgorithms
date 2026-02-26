import sys


class CustomPhoneSet:
    def __init__(self, max_elements: int):
        #(load factor < 0.5)
        self.capacity = 200003
        self.table = [None] * self.capacity
        self.unique_count = 0

    def insert(self, phone_number: str):
        idx = int(phone_number) % self.capacity

        while self.table[idx] is not None:
            if self.table[idx] == phone_number:
                return
            idx = (idx + 1) % self.capacity

        self.table[idx] = phone_number
        self.unique_count += 1


def solve():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    phone_book = CustomPhoneSet(n)
    for i in range(1, n + 1):
        phone_book.insert(input_data[i])
    print(phone_book.unique_count)

if __name__ == '__main__':
    solve()