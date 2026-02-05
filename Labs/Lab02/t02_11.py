def f(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

def g(n):
    sum = 0                         # O(1)
    for i in range(1, n + 1):       # O(n)
        sum = sum + i + f(i)        # O(n^2)
    return sum                      # O(1)
                                    # T(n) = O(n^2)

#Програма рахує суму (n + n(n+1)/2) = (n^2 + 3n)/2 = 1/2 * n(n + 1)(2n + 1)/6 + 3/2 * n(n+1)/2 =
# = n(n+1)(n+5)/6

def h(n):
    return n * (n + 1) * (n + 5) // 6 # O(1)