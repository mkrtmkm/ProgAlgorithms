import sys

sys.setrecursionlimit(60000)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build(path, index, min_val, max_val):
    if index[0] >= len(path):
        return True, None

    val = path[index[0]]

    if val < min_val or val > max_val:
        return False, None

    node = Node(val)
    index[0] += 1

    if index[0] == len(path):
        return True, node

    next_val = path[index[0]]

    if next_val < val:
        is_valid, node.left = build(path, index, min_val, val - 1)
        return is_valid, node
    else:
        is_valid, node.right = build(path, index, val + 1, max_val)
        return is_valid, node


def main():
    data = sys.stdin.read().split()
    if not data:
        print("YES")
        return

    path = [int(x) for x in data]

    index = [0]

    min_val = float('-inf')
    max_val = float('inf')

    is_valid, root = build(path, index, min_val, max_val)

    if is_valid and index[0] == len(path):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()