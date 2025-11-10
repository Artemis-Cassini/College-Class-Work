# Read the first line of positive integers
user_values = list(map(int, input().split()))

# Read the negative integer (N)
neg = int(input())

N = abs(neg)

# If the list is smaller than N → output the original negative integer
if len(user_values) < N:
    print(neg)
else:
    print(user_values[-N])