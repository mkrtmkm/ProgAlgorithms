import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return

    m = int(input[0])
    n = int(input[1])
    maze = [list(input[i]) for i in range(2, 2 + m)]
    parts_count = 0

    for i in range(m):
        for j in range(n):
            if maze[i][j] == '#':
                parts_count += 1
                stack = [(i, j)]
                maze[i][j] = '.'

                while stack:
                    r, c = stack.pop()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '#':
                            maze[nr][nc] = '.'
                            stack.append((nr, nc))

    print(parts_count)

if __name__ == "__main__":
    solve()