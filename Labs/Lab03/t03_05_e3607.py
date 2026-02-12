import sys

while True:
    cnt = 0
    line = sys.stdin.readline()
    if not line:
        break

    n = int(line.strip())
    arr = list(map(int, sys.stdin.readline().split()))
    a, b = map(int, sys.stdin.readline().split())

    for el in arr:
        if a <= el <= b:
            cnt += 1
    print(cnt)
