def a(n, k):
    k += 1              # 4
    i = n               # 2
    while i > 0:        # 3 * (n + 1)
        i -= 1          # 4 * n
                        # T(n) = 7n + 9

def b(n, k):
    i = n               # 2
    while i > 1:        # 3 * ([log n] + 1)
        k += 1          # 4 * [log n]
        i //= 2         # 4 * [log n]
                        # T(n) = 11log n + 5

def c(n, k):
    i = 0               # 2
    while i < n:        # 3 * ([(n + 1)/2] + 1)
        j = 0           # 2 * [(n + 1)/2]
        while j < n:    # 3 * [(n + 1)/2] * ([(n + 1)/2] + 1)
            k += 1      # 4 * [(n + 1)/2]^2
            j += 2      # 4 * [(n + 1)/2]^2
        i += 2          # 4 * [(n + 1)/2]
                        #T(n) = 11 * [(n + 1)/2]^2 + 9 * [(n + 1)/2] + 5
# while i < n:              |   while j < n:
# n = 0, cond = 1, loop = 0 |   Аналогічно з попереднім
# n = 1, cond = 2, loop = 1 |
# n = 2, cond = 2, loop = 1 |
# n = 3, cond = 3, loop = 2 |
# n = 4, cond = 3, loop = 2 |

def d(n, k):
    i = 0               # 2
    while i < n:        # 3 * (n + 1)
        j = 0           # 2 * n
        while j < i*i:  # 5 * (N + n)
            k += 1      # 4 * N
            j += 1      # 4 * N
        i += 1          # 4 * n
                        # T(n) = 13 * N + 14 * n + 5 = 13/6 * n(n-1)(2n-1) + 14 * n + 5

# while i < n:              |   while j < i*i:
# n = 0, cond = 1, loop = 0 |   n = 0, cond = 0, loop = 0
# n = 1, cond = 2, loop = 1 |   n = 1, cond = 1, loop = 0
# n = 2, cond = 3, loop = 2 |   n = 2, cond = 3, loop = 1
# n = 3, cond = 4, loop = 3 |   n = 3, cond = 8, loop = 5
# n = 4, cond = 5, loop = 4 |   n = 4, cond = 20, loop =  17
#                               loop = sum(i^2) for i in range(n) = N = n(n-1)(2n-1)/6
#                               cond = sum(i^2 + 1) for i in range(n) = N + n

def e(n, k):
    i = 1               # 2
    while i < n:        # 3 * ([log n] + 1)
        j = 1           # 2 * [log n]
        while j < n:    # 3 * [log n] * ([log n] + 1)
            k += 1      # 4 * [log n]^2
            j *= 2      # 4 * [log n]^2
        i *= 2          # 4 * [log n]
                        # T(n) = 11 * [log n]^2 + 12 * [log n] + 5

def f(n, k):
    i = 1               # 2
    while i < n:        # 3 * ([log n] + 1)
        j = i           # 3 * [log n]
        while j < n:    # 3 * ([log n] + ([log n] - 1) + ([log n] - 2) + ... + 1) = 3 * [log n] * (1 + ([log n] + 1)/2)
            k += 1      # 4 * [log n] * ([log n] + 1)/2
            j *= 2      # 4 * [log n] * ([log n] + 1)/2
        i *= 2          # 3 * [log n]
                        # T(n) = 5/2 * [log n]^2 + 17/2 [log n] + 5