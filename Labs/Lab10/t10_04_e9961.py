def permutations(n, k):
    current_sequence = []

    def gen():
        if len(current_sequence) == k:
            if len(set(current_sequence)) == k:
                print(" ".join(map(str, current_sequence)))
            return

        for i in range(1, n + 1):
            current_sequence.append(i)
            gen()
            current_sequence.pop()

    gen()

if __name__ == "__main__":
    n, k = map(int, input().split())
    permutations(n, k)