import sys

def main():
    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    matrix_elements = input[1:]

    hanging_count = 0

    for i in range(n):
        row = matrix_elements[i * n: (i + 1) * n]
        degree = sum(int(x) for x in row)
        if degree == 1:
            hanging_count += 1

    print(hanging_count)

if __name__ == '__main__':
    main()