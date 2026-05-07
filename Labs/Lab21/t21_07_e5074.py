import sys

def main():
    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    m = int(input[1])
    degrees = [0] * (n + 1)

    idx = 2
    for _ in range(m):
        u = int(input[idx])
        v = int(input[idx + 1])
        degrees[u] += 1
        degrees[v] += 1

        idx += 2

    for i in range(1, n + 1):
        print(degrees[i])

if __name__ == '__main__':
    main()