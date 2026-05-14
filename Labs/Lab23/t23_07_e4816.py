import sys

class Graph:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj

    def get_components(self):
        visited = [False] * (self.n + 1)
        components = []

        for i in range(1, self.n + 1):
            if not visited[i]:
                current_component = []
                stack = [i]
                visited[i] = True

                while stack:
                    curr = stack.pop()
                    current_component.append(curr)

                    for neighbor in self.adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)

                components.append(current_component)
        return components


if __name__ == "__main__":
    input = sys.stdin.read().split()
    if not input:
        sys.exit()

    n = int(input[0])
    m = int(input[1])
    adj = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        u = int(input[idx])
        v = int(input[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    graph = Graph(n, adj)
    components = graph.get_components()

    print(len(components))
    for comp in components:
        print(len(comp))
        print(*(comp))