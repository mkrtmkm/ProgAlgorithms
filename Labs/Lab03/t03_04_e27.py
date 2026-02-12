n = int(input())

binary_s = bin(n)[2:]
length = len(binary_s)
max_val = n
current_s = binary_s

for _ in range(length - 1):
    current_s = current_s[1:] + current_s[0]
    current_val = int(current_s, 2)
    if current_val > max_val:
        max_val = current_val
print(max_val)
