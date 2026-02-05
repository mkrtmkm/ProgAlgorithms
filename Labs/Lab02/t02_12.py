# h(n) = f(n) + g(n) => h(n) = O(max(f, g)) = O(n^2)

# Res = 3n(n+1)/6 + n(n+1)(n+5)/6 = n(n+1)(n+8)/6

def j(n):
    return n * (n + 1) * (n + 8) // 6 # O(1)

