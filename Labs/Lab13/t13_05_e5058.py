def check_brackets(sequence: str) -> str:
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for char in sequence:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != brackets[char]:
                return "no"

    return "yes" if not stack else "no"

if __name__ == "__main__":
    sequence = input().strip()
    print(check_brackets(sequence))