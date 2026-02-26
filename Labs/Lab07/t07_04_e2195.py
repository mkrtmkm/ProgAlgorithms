import sys

class CustomHashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.used = [False] * self.capacity

    def _hash(self, word: str) -> int:
        h = 516
        for char in word:
            h = ((h << 3) + h) + ord(char)
        return h % self.capacity

    def insert(self, word: str):
        idx = self._hash(word)

        while self.keys[idx] is not None:
            if self.keys[idx] == word:
                return
            idx = (idx + 1) % self.capacity
        self.keys[idx] = word

    def mark_used_and_check(self, word: str) -> bool:
        idx = self._hash(word)

        while self.keys[idx] is not None:
            if self.keys[idx] == word:
                self.used[idx] = True
                return True
            idx = (idx + 1) % self.capacity
        return False

    def all_words_used(self) -> bool:
        for i in range(self.capacity):
            if self.keys[i] is not None and self.used[i] == False:
                return False
        return True


def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    first_line = input_data[0].split()
    n = int(first_line[0])
    ht = CustomHashTable(2003)

    for i in range(1, n + 1):
        ht.insert(input_data[i].strip().lower())
    current_word_chars = []

    for line_idx in range(n + 1, len(input_data)):
        line = input_data[line_idx]
        for char in line:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                current_word_chars.append(char.lower())
            else:
                if current_word_chars:
                    word = "".join(current_word_chars)
                    if not ht.mark_used_and_check(word):
                        print("Some words from the text are unknown.")
                        return

                    current_word_chars.clear()
        if current_word_chars:
            word = "".join(current_word_chars)
            if not ht.mark_used_and_check(word):
                print("Some words from the text are unknown.")
                return
            current_word_chars.clear()
    if not ht.all_words_used():
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")

if __name__ == '__main__':
    solve()