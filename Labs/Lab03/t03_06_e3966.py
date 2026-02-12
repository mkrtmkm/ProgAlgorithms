import sys

input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for x in b:
    if x in a:
        print("YES")
    else:
        print("NO")