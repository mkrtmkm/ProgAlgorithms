n, k = map(int, input().split())
stalls = list(map(int, input().split()))

stalls.sort()

def can_place(stalls, k, dist):
    count = 1
    last = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last >= dist:
            count += 1
            last = stalls[i]
            if count == k:
                return True
    return False

left = 1
right = stalls[-1] - stalls[0]
best = 0

while left <= right:
    mid = (left + right) // 2
    if can_place(stalls, k, mid):
        best = mid
        left = mid + 1
    else:
        right = mid - 1

print(best)
