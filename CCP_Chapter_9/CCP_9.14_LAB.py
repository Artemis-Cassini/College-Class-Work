num = int(input())

reverse_binary = ""
while num > 0:
    bit = num % 2            # get the remainder (either 0 or 1)
    reverse_binary += str(bit)
    num = num // 2           # integer divide by 2 to move to the next bit

print(reverse_binary)
