import sys

class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = {}

    def add_path(self, path_parts):
        if not path_parts:
            return

        first_dir = path_parts[0]
        if first_dir not in self.subdirectories:
            self.subdirectories[first_dir] = Directory(first_dir)

        self.subdirectories[first_dir].add_path(path_parts[1:])

    def display(self, depth=0):
        if self.name != "":
            print(" " * depth + self.name)
            next_depth = depth + 1
        else:
            next_depth = 0

        sorted_names = sorted(self.subdirectories.keys())

        for name in sorted_names:
            self.subdirectories[name].display(next_depth)

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0])
    paths = input_data[1:n + 1]
    root = Directory("")

    for path in paths:
        parts = path.split('\\')
        root.add_path(parts)
    root.display()

if __name__ == "__main__":
    solve()