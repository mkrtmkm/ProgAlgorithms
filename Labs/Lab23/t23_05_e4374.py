import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    m = int(input[1])
    adj = [[] for _ in range(n + 1)]

    idx = 2
    for i in range(1, m + 1):
        u = int(input[idx])
        v = int(input[idx + 1])
        idx += 2
        adj[u].append((v, i))
        adj[v].append((u, i))

    k = int(input[idx])
    idx += 1
    deleted = [False] * (m + 1)
    out = []

    for _ in range(k):
        c = int(input[idx])
        idx += 1

        del_edges = []
        for _ in range(c):
            edge_idx = int(input[idx])
            idx += 1
            del_edges.append(edge_idx)
            deleted[edge_idx] = True

        visited = [False] * (n + 1)
        stack = [1]
        visited[1] = True
        count = 1

        while stack:
            u = stack.pop()

            for v, edge_id in adj[u]:
                if not deleted[edge_id] and not visited[v]:
                    visited[v] = True
                    count += 1
                    stack.append(v)

        if count == n:
            out.append("Connected")
        else:
            out.append("Disconnected")

        for edge_idx in del_edges:
            deleted[edge_idx] = False

    print('\n'.join(out))

if __name__ == '__main__':
    solve()