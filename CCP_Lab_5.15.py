# read 4 floats
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

# compute product and average
product = n1 * n2 * n3 * n4
average = (n1 + n2 + n3 + n4) / 4

# output rounded integers
print(f"{product:.0f} {average:.0f}")

# output with 3 decimals
print(f"{product:.3f} {average:.3f}")