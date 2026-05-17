import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    m = int(input[1])

    # координати
    x1 = int(input[-4]) - 1
    y1 = int(input[-3]) - 1
    x2 = int(input[-2]) - 1
    y2 = int(input[-1]) - 1

    maze_chars = []
    for _ in input[2:-4]:
        maze_chars.extend(list(_))

    maze = [maze_chars[i * m: (i + 1) * m] for i in range(n)]
    if y1 == y2 and x1 == x2:
        print(0)
        return

    queue = deque([(y1, x1, 0)])
    maze[y1][x1] = '1'
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, dist = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if nr == y2 and nc == x2:
                print(dist + 1)
                return

            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == '0':
                maze[nr][nc] = '1'
                queue.append((nr, nc, dist + 1))

    print("-1")

if __name__ == "__main__":
    solve()
