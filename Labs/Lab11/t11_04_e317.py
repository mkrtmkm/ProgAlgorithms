import sys

sys.set_int_max_str_digits(1000000)
sys.setrecursionlimit(1000)

def karatsuba(x, y):
    if x < 10**100 or y < 10**100:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # x = x1 * 10^m + x2
    # y = y1 * 10^m + y2
    x1, x2 = divmod(x, 10**m)
    y1, y2 = divmod(y, 10**m)

    z2 = karatsuba(x1, y1)           # ac
    z0 = karatsuba(x2, y2)           # bd
    z1 = karatsuba(x1 + x2, y1 + y2) # (a+b)(c+d)

    return (z2 * 10**(2 * m)) + ((z1 - z2 - z0) * 10**m) + z0

if __name__ == "__main__":
    input = sys.stdin.read().split()
    x = int(input[0])
    y = int(input[1])
    print(karatsuba(x, y))
