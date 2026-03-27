import sys

def solve():
    input = sys.stdin.read().split()
    idx = 0

    while idx < len(input):
        n = int(input[idx])
        idx += 1
        if n == 0:
            break

        while True:
            if int(input[idx]) == 0:
                idx += 1
                print()
                break

            target = [int(x) for x in input[idx: idx + n]]
            idx += n

            stack = []
            current_car = 1
            possible = True

            for car_needed in target:
                while (not stack or stack[-1] != car_needed) and current_car <= n:
                    stack.append(current_car)
                    current_car += 1

                if stack and stack[-1] == car_needed:
                    stack.pop()
                else:
                    possible = False
                    break

            if possible:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    solve()