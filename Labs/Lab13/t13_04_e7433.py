def convert(number: str, to_base: int) -> str:
    decimal = int(number)

    if decimal == 0:
        return "0"

    stack = []
    while decimal > 0:
        stack.append(
            decimal % to_base
        )
        decimal //= to_base

    res = ""
    while stack:
        res += get_char(stack.pop())

    return res


def get_char(n: int) -> str:
    if n < 10:
        return str(n)
    else:
        return f"[{n}]"


if __name__ == "__main__":
    num = input().strip()
    base = int(input().strip())

    print(convert(num, base))