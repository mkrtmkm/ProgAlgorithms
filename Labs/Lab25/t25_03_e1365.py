import sys

def main():
    data = sys.stdin.read().split()
    pos = 0
    n = int(data[pos]); pos += 1
    s = int(data[pos]); pos += 1
    f = int(data[pos]); pos += 1

    g = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(data[pos])); pos += 1
        g.append(row)

    INF = float('inf')
    dist = [INF] * n
    used = [False] * n

    s -= 1
    f -= 1
    dist[s] = 0

    for step in range(n):
        v = -1
        for i in range(n):
            if not used[i] and dist[i] != INF:
                if v == -1 or dist[i] < dist[v]:
                    v = i

        if v == -1:
            break

        used[v] = True

        for j in range(n):
            w = g[v][j]
            if w != -1:
                if dist[v] + w < dist[j]:
                    dist[j] = dist[v] + w

    if dist[f] == INF:
        print(-1)
    else:
        print(dist[f])

if __name__ == "__main__":
    main()