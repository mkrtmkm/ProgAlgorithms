def lower_bound(arr, x):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l


def upper_bound(arr, x):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return l


n = int(input())
colors = list(map(int, input().split()))
m = int(input())
to_check = list(map(int, input().split()))

for x in to_check:
    left = lower_bound(colors, x)
    right = upper_bound(colors, x)
    print(right - left)