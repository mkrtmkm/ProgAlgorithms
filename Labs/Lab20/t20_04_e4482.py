import sys

sys.setrecursionlimit(200000)

INF = float('inf')
tree_min = []
tree_max = []


def BuildTree(a, v, lpos, rpos):
    if lpos == rpos:
        tree_min[v] = a[lpos]
        tree_max[v] = a[lpos]
    else:
        mid = (lpos + rpos) // 2
        BuildTree(a, 2 * v, lpos, mid)
        BuildTree(a, 2 * v + 1, mid + 1, rpos)

        tree_min[v] = min(tree_min[2 * v], tree_min[2 * v + 1])
        tree_max[v] = max(tree_max[2 * v], tree_max[2 * v + 1])


def GetMin(v, lpos, rpos, left, right):
    if left > right:
        return INF
    if left == lpos and right == rpos:
        return tree_min[v]

    mid = (lpos + rpos) // 2
    return min(
        GetMin(2 * v, lpos, mid, left, min(right, mid)),
        GetMin(2 * v + 1, mid + 1, rpos, max(left, mid + 1), right))


def GetMax(v, lpos, rpos, left, right):
    if left > right:
        return -INF
    if left == lpos and right == rpos:
        return tree_max[v]

    mid = (lpos + rpos) // 2
    return max(
        GetMax(2 * v, lpos, mid, left, min(right, mid)),
        GetMax(2 * v + 1, mid + 1, rpos, max(left, mid + 1), right))


def Update(v, lpos, rpos, pos, val):
    if lpos == rpos:
        tree_min[v] = val
        tree_max[v] = val
    else:
        mid = (lpos + rpos) // 2
        if pos <= mid:
            Update(2 * v, lpos, mid, pos, val)
        else:
            Update(2 * v + 1, mid + 1, rpos, pos, val)

        tree_min[v] = min(tree_min[2 * v], tree_min[2 * v + 1])
        tree_max[v] = max(tree_max[2 * v], tree_max[2 * v + 1])


def solve():
    global tree_min, tree_max

    input = sys.stdin.read().split()
    if not input:
        return

    n = int(input[0])
    v = [0] + [int(x) for x in input[1:n + 1]]

    tree_min = [0] * (4 * n + 4)
    tree_max = [0] * (4 * n + 4)

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
            segment_min = GetMin(1, 1, n, l, r)
            segment_max = GetMax(1, 1, n, l, r)

            if segment_min == segment_max:
                out.append("draw")
            else:
                out.append("wins")
        else:
            Update(1, 1, n, l, r)

    print('\n'.join(out))


if __name__ == '__main__':
    solve()