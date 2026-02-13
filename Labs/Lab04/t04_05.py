def f(x):
    return x**3 + 4 * x**2 + x - 6

left = 0.0
right = 2.0
epsilon = 10e-5

while right - left > epsilon:
    mid = (left + right) / 2
    if f(mid) < 0:
        left = mid
    else:
        right = mid

print(f"{right:.6f}")