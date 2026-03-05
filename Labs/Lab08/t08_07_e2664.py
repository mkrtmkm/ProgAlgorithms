def insertion_sort(n, array):
    is_sorted = True
    for i in range(1, n):
        if array[i] < array[i - 1]:
            is_sorted = False
            break

    if is_sorted:
        return

    for index in range(1, n):
        currentValue = array[index]
        position = index

        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
            else:
                break
            position -= 1

        array[position] = currentValue
        if position != index:
            print(" ".join(map(str, array)))

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    insertion_sort(n, array)