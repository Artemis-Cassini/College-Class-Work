numbers = list(map(int, input().split()))

lower_bound, upper_bound = map(int, input().split())

result = [num for num in numbers if lower_bound <= num <= upper_bound]

print(",".join(map(str, result)), end=",")