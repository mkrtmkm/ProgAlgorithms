def quick_sort(array, a, b):
    if a >= b:
        return

    pivot = array[a + (b - a) // 2]
    left = a
    right = b

    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    quick_sort(array, a, right)
    quick_sort(array, left, b)


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    quick_sort(array, 0, n - 1)
    print(*array)