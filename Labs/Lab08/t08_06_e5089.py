def selection_sort(n, array):
    for i in range(n - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if array[maxpos] < array[j]:
                maxpos = j
        array[i], array[maxpos] = array[maxpos], array[i]

if __name__ == "__main__":
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input().strip())

    selection_sort(n, words)

    for word in words:
        print(word)