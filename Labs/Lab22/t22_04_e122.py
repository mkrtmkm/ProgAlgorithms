import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    k = int(input[1])
    start_node = int(input[2])
    end_node = int(input[3])
    max_d = int(input[4])

    adj = {i: [] for i in range(1, n + 1)}

    idx = 5
    for _ in range(k):
        u = int(input[idx])
        v = int(input[idx + 1])
        adj[u].append(v)
        idx += 2

    visited = [False] * (n + 1)
    paths_count = 0

    def dfs(u, current_d):
        nonlocal paths_count

        if u == end_node:
            paths_count += 1
            return

        if current_d == max_d:
            return

        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v, current_d + 1)

        visited[u] = False

    dfs(start_node, 0)
    print(paths_count)

if __name__ == '__main__':
    solve()