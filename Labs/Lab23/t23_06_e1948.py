import sys
from collections import deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n + 1)]
        self.in_degree = [0] * (n + 1)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.in_degree[v] += 1

    def topological_sort(self):
        queue = deque()
        for i in range(1, self.n + 1):
            if self.in_degree[i] == 0:
                queue.append(i)

        topo_order = []
        while queue:
            u = queue.popleft()
            topo_order.append(u)

            for v in self.adj[u]:
                self.in_degree[v] -= 1
                if self.in_degree[v] == 0:
                    queue.append(v)

        if len(topo_order) == self.n:
            return topo_order
        else:
            return []


if __name__ == "__main__":
    input = sys.stdin.read().split()
    if not input:
        sys.exit()

    n = int(input[0])
    m = int(input[1])
    graph = Graph(n)

    idx = 2
    for _ in range(m):
        u = int(input[idx])
        v = int(input[idx + 1])
        idx += 2
        graph.add_edge(u, v)

    result = graph.topological_sort()
    if result:
        print(*(result))
    else:
        print("-1")