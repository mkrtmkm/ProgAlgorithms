import sys

def solve(idx, current_sum, current_path):
    global best_sum, best_path, N, s, tracks
    if current_sum > N:
        return

    if current_sum > best_sum:
        best_sum = current_sum
        best_path = current_path[:]

    if best_sum == N:
        return

    for i in range(idx, s):
        if current_sum + tracks[i] <= N:
            current_path.append(tracks[i])
            solve(i + 1, current_sum + tracks[i], current_path)
            current_path.pop()

            if best_sum == N:
                return

if __name__ == "__main__":
    input = sys.stdin.read().splitlines()

    for line in input:
        parts = list(map(int, line.split()))
        if len(parts) < 2:
            continue

        N = parts[0]  # Місткість касети
        s = parts[1]  # Кількість треків
        tracks = parts[2:2 + s]  # Тривалості треків

        best_sum = 0
        best_path = []

        solve(0, 0, [])

        print(f"sum:{best_sum}")