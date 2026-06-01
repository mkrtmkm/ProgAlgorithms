import math
import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    coords = []
    for _ in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))

    if n == 1:
        print("0.0000000000")
        return

    def dist(i, j):
        dx = coords[i][0] - coords[j][0]
        dy = coords[i][1] - coords[j][1]
        return math.sqrt(dx * dx + dy * dy)

    INF = float('inf')

    key = [INF] * n
    in_mst = [False] * n

    key[0] = 0.0
    total = 0.0

    for _ in range(n):
        u = -1
        for v in range(n):
            if not in_mst[v]:
                if u == -1 or key[v] < key[u]:
                    u = v

        in_mst[u] = True
        total += key[u]

        for v in range(n):
            if not in_mst[v]:
                d = dist(u, v)
                if d < key[v]:
                    key[v] = d
    print(f"{total:.10f}")

if __name__ == "__main__":
    solve()