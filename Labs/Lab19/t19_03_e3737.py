import sys

def is_min_heap(elements, n):
    for i in range(1, n // 2 + 1):
        left_idx = 2 * i
        right_idx = 2 * i + 1

        if left_idx <= n and elements[i] > elements[left_idx]:
            return False

        if right_idx <= n and elements[i] > elements[right_idx]:
            return False
    return True

def solve():
    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    elements = [0] * (n + 1)

    for i in range(1, n + 1):
        elements[i] = int(input[i])

    if is_min_heap(elements, n):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()