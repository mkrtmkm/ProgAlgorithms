import math

def f(x):
    return math.sin(x) - x / 3

left = 1.6
right = 3.0
epsilon = 10e-5

while right - left > epsilon:
    mid = (left + right) / 2
    if f(mid) > 0:
        left = mid
    else:
        right = mid

print(f"{right:.6f}")