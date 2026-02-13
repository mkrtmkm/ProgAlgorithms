import math

try:
    c = float(input())
    eps = 10e-5

    left = 0.0
    right = 10e10

    while right - left > eps:
        mid = (left + right) / 2
        val = mid * mid + math.sqrt(mid)

        if val < c:
            left = mid
        else:
            right = mid

    print(f"{right:.6f}")

except (EOFError, ValueError):
    pass
