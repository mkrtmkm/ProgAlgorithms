import sys

def main():
    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    m = int(input[1])
    unique_edges = set()
    idx = 2

    for _ in range(m):
        u = int(input[idx])
        v = int(input[idx + 1])
        if u != v:
            edge = (min(u, v), max(u, v))
            unique_edges.add(edge)

        idx += 2

    required_edges = n * (n - 1) // 2
    if len(unique_edges) == required_edges:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()