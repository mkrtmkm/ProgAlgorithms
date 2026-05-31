INF = 30000

n, m = map(int, input().split())

edges = []
for i in range(m):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))

dist = [INF] * (n + 1)
dist[1] = 0

for i in range(n - 1):
    for a, b, w in edges:
        if dist[a] != INF and dist[a] + w < dist[b]:
            dist[b] = dist[a] + w

answer = []
for v in range(1, n + 1):
    answer.append(str(dist[v]))

print(' '.join(answer))