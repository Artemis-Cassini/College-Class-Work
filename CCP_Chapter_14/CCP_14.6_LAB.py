user_values = []   # List of integers from input
# Type your code here.

length = int(input())

for _ in range(length):
    user_values.append(int(input()))

if user_values == user_values[::-1]:
    print("yes")
else:
    print("no")