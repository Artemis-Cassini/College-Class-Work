numbers = list(map(int, input().split()))

negative_numbers = sorted([num for num in numbers if num < 0], reverse=True)

print(" ".join(map(str, negative_numbers)), end=" ")