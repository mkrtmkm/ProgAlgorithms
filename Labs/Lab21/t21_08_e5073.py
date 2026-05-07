import sys

def main():
    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    m = int(input[1])
    seen_edges = set()
    idx = 2

    for _ in range(m):
        u = int(input[idx])
        v = int(input[idx + 1])
        edge = (u, v)

        if edge in seen_edges:
            print("YES")
            return

        seen_edges.add(edge)
        idx += 2

    print("NO")

if __name__ == '__main__':
    main()