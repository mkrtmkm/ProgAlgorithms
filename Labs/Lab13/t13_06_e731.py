import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    expr = input_data[0]

    stack = []
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}

    for char in reversed(expr):
        if char in "+-*/":
            l_str, l_op = stack.pop()
            r_str, r_op = stack.pop()

            p = prec[char]

            if l_op and prec[l_op] < p:
                l_str = f"({l_str})"

            if r_op:
                if prec[r_op] < p:
                    r_str = f"({r_str})"
                elif prec[r_op] == p and char in ('-', '/'):
                    r_str = f"({r_str})"
            stack.append((f"{l_str}{char}{r_str}", char))
        else:
            stack.append((char, None))

    result_expr, _ = stack.pop()
    print(result_expr)

if __name__ == '__main__':
    solve()