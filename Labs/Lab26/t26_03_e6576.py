import heapq
import sys

def solve():
    input = sys.stdin.readline
    n, m, p, q = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    target_w = None

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))
        if (u == p and v == q) or (u == q and v == p):
            target_w = w

    if target_w is None:
        print("NO")
        return

    in_mst = [False] * (n + 1)
    mst_edges = set()
    heap = [(0, 1, -1)]

    while heap:
        w, u, parent = heapq.heappop(heap)

        if in_mst[u]:
            continue

        in_mst[u] = True

        if parent != -1:
            mst_edges.add((min(parent, u), max(parent, u)))

        for edge_w, v in graph[u]:
            if not in_mst[v]:
                heapq.heappush(heap, (edge_w, v, u))

    edge = (min(p, q), max(p, q))
    if edge in mst_edges:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()