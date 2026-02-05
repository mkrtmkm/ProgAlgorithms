def a(n):
    sum = 0                         # O(1)
    for i in range(1, n + 1):       # O(n)
        sum += i                    # O(n)
    return sum                      # O(1)
                                    # T(n) = O(n)

def b(n):
    sum = 0                         # O(1)
    for i in range(1, n + 1):       # O(n)
        sum += i * i                # O(n)
    return sum                      # O(1)
                                    # T(n) = O(n)

def c(n, a):
    sum = 0                         # O(1)
    pow_a = 1                       # O(1)
    for i in range(1, n + 1):       # O(n)
        sum += pow_a                # O(n)
        pow_a *= a                  # O(n)
    return sum                      # O(1)
                                    # T(n) = O(n)

def d(n):
    sum = 0                         # O(1)
    for i in range(n + 1):          # O(n)
        val = 1                     # O(n)
        for k in range(i):          # O(n^2)
            val *= i                # O(n^2)
        sum += val                  # O(n)
    return sum                      # O(1)
                                    # T(n) = O(n^2)

def e(n):
    res = 1                         # O(1)
    for i in range(1, n + 1):       # O(n)
        term = 1 / (1 + i)          # O(n)
        res *= term                 # O(n)
    return res                      # O(1)
                                    # T(n) = O(n)

def f(n):
    res = 1                         # O(1)
    fact = 1                        # O(1)
    for i in range(1, n + 1):       # O(n)
        fact *= i                   # O(n)
        term = 1 / (1 + fact)       # O(n)
        res *= term                 # O(n)
    return res                      # O(1)
                                    # T(n) = O(n)


def g(n, a):
    res = 1                         # O(1)
    pow_a = 1                       # O(1)
    fact = 1                        # O(1)
    for i in range(1, n + 1):       # O(n)
        pow_a *= a                  # O(n)
        fact *= i                   # O(n)
        term = pow_a / (1 + fact)   # O(n)
        res *= term                 # O(n)
    return res                      # O(1)
                                    # T(n) = O(n)


def h(n, m):
    res = 1                         # O(1)
    for i in range(1, n + 1):       # O(n)
        pow_val = 1                 # O(n)
        for k in range(m):          # O(m)
            pow_val *= i            # O(nm)
        term = 1 / (1 + pow_val)    # O(n)
        res *= term                 # O(n)
    return res                      # O(1)
                                    # T(n) = O(nm)


def i(n):
    res = 1                         # O(1)
    for i in range(1, n + 1):       # O(n)
        pow_val = 1                 # O(n)
        for k in range(i):          # O(n^2)
            pow_val *= i            # O(n^2)
        term = 1 / (1 + pow_val)    # O(n)
        res *= term                 # O(n)
    return res                      # O(1)
                                    # T(n) = O(n^2)