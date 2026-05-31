import sys

def main():
    data = sys.stdin.read().split()
    pos = 0
    n = int(data[pos]); pos += 1

    d = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(data[pos])); pos += 1
        d.append(row)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

    out = []
    for i in range(n):
        out.append(' '.join(str(d[i][j]) for j in range(n)))
    print('\n'.join(out))

if __name__ == "__main__":
    main()