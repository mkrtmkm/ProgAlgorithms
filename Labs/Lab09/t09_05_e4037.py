import sys

def merge_sort(array):
    if len(array) > 1:
        m = len(array) // 2
        left = array[:m]
        right = array[m:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    input = sys.stdin.read().split()

    n = int(input[0])

    array = []
    idx = 1
    for _ in range(n):
        array.append((int(input[idx]), int(input[idx + 1])))
        idx += 2
    merge_sort(array)

    output = []
    for robot in array:
        output.append(f"{robot[0]} {robot[1]}")

    print('\n'.join(output))