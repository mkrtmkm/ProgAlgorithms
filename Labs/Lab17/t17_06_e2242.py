import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    return root


def preorder(root, result):
    if root:
        result.append(root.key)
        preorder(root.left, result)
        preorder(root.right, result)


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    batches = []
    for line in data:
        if line == '*':
            break
        batches.append(line)

    root = None

    for batch in reversed(batches):
        for char in batch:
            root = insert(root, char)

    result = []
    preorder(root, result)

    if result:
        print("".join(result))


if __name__ == '__main__':
    main()