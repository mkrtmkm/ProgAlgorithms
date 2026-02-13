def f(x):
    return x ** 3 + x + 1

eps = 10e-5
target = 5.0
left = 0.0
right = 10.0

while right - left > eps:
    mid = (left + right) / 2
    if f(mid) < target:
        left = mid
    else:
        right = mid

print(f"{right:.5f}")