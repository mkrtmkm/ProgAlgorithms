import sys
import math

sys.setrecursionlimit(200000)

SegTree = []


def gcd(a, b):
    return math.gcd(a, b)


def BuildTree(a, v, lpos, rpos):
    if lpos == rpos:
        SegTree[v] = a[lpos]
    else:
        mid = (lpos + rpos) // 2
        BuildTree(a, 2 * v, lpos, mid)
        BuildTree(a, 2 * v + 1, mid + 1, rpos)
        SegTree[v] = gcd(SegTree[2 * v], SegTree[2 * v + 1])


def GetGCD(v, lpos, rpos, left, right):
    if left > right:
        return 0
    if left == lpos and right == rpos:
        return SegTree[v]
    mid = (lpos + rpos) // 2
    return gcd(
        GetGCD(2 * v, lpos, mid, left, min(right, mid)),
        GetGCD(2 * v + 1, mid + 1, rpos, max(left, mid + 1), right)
    )


def Update(v, lpos, rpos, pos, val):
    if lpos == rpos:
        SegTree[v] = val
    else:
        mid = (lpos + rpos) // 2
        if pos <= mid:
            Update(2 * v, lpos, mid, pos, val)
        else:
            Update(2 * v + 1, mid + 1, rpos, pos, val)
        SegTree[v] = gcd(SegTree[2 * v], SegTree[2 * v + 1])


def solve():
    global SegTree

    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    v = [0] + [int(x) for x in input[1:n + 1]]

    SegTree = [0] * (4 * n + 4)
    BuildTree(v, 1, 1, n)

    m = int(input[n + 1])
    queries = input[n + 2:]
    idx = 0
    out = []

    for _ in range(m):
        q = int(queries[idx])
        l = int(queries[idx + 1])
        r = int(queries[idx + 2])
        idx += 3

        if q == 1:
            out.append(str(GetGCD(1, 1, n, l, r)))
        else:
            Update(1, 1, n, l, r)

    print('\n'.join(out))


if __name__ == '__main__':
    solve()