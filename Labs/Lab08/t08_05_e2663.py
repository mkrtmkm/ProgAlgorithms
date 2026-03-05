def count(n, array):
    count = 0
    for i in range(n-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                count += 1

    return count

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    print(count(n, array))