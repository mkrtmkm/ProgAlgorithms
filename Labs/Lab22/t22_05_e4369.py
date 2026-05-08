import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    m = int(input[1])
    adj = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        u = int(input[idx])
        v = int(input[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    k = int(input[idx])
    idx += 1
    queue = []
    dist = [-1] * (n + 1)

    for _ in range(k):
        source = int(input[idx])
        idx += 1
        queue.append(source)
        dist[source] = 0

    max_time = 0
    head = 0

    while head < len(queue):
        u = queue[head]
        head += 1

        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                if dist[v] > max_time:
                    max_time = dist[v]
                queue.append(v)

    last_burned_node = -1
    for i in range(1, n + 1):
        if dist[i] == max_time:
            last_burned_node = i
            break

    print(max_time)
    print(last_burned_node)

if __name__ == '__main__':
    solve()