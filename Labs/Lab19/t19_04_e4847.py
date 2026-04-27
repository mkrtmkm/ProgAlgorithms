import sys


class Heap:
    def __init__(self):
        self._items = []
        self.pos = {}

    def insert(self, item_id: str, priority: int):
        self._items.append([priority, item_id])
        self.pos[item_id] = len(self._items) - 1
        self.siftUp(len(self._items) - 1)

    def extract_maximum(self) -> tuple[str, int]:
        max_item = self._items[0]

        if len(self._items) == 1:
            item = self._items.pop()
            del self.pos[item[1]]
            return item[1], item[0]

        self.swap(0, len(self._items) - 1)
        item = self._items.pop()
        del self.pos[max_item[1]]
        self.siftDown(0)

        return max_item[1], max_item[0]

    def change(self, item_id: str, new_priority: int):
        idx = self.pos[item_id]
        old_priority = self._items[idx][0]
        self._items[idx][0] = new_priority

        if new_priority > old_priority:
            self.siftUp(idx)
        elif new_priority < old_priority:
            self.siftDown(idx)

    def swap(self, idx1, idx2):
        id1 = self._items[idx1][1]
        id2 = self._items[idx2][1]
        self.pos[id1], self.pos[id2] = idx2, idx1
        self._items[idx1], self._items[idx2] = self._items[idx2], self._items[idx1]

    def siftUp(self, idx):
        i = idx
        while i > 0:
            parent = (i - 1) // 2
            if self._items[parent][0] >= self._items[i][0]:
                break
            self.swap(i, parent)
            i = parent

    def siftDown(self, idx):
        i = idx
        n = len(self._items)

        while 2 * i + 1 < n:
            left = 2 * i + 1
            right = 2 * i + 2

            if right < n and self._items[left][0] < self._items[right][0]:
                max_child = right
            else:
                max_child = left

            if self._items[max_child][0] <= self._items[i][0]:
                break

            self.swap(i, max_child)
            i = max_child


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    heap = MaxHeap()
    out = []
    idx = 0

    while idx < len(data):
        cmd = data[idx]
        if cmd == "ADD":
            heap.insert(data[idx + 1], int(data[idx + 2]))
            idx += 3
        elif cmd == "POP":
            item_id, prio = heap.extract_maximum()
            out.append(f"{item_id} {prio}")
            idx += 1
        elif cmd == "CHANGE":
            heap.change(data[idx + 1], int(data[idx + 2]))
            idx += 3

    if out:
        print('\n'.join(out))


if __name__ == "__main__":
    solve()