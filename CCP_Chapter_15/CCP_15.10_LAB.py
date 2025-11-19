numbers = list(map(int, input().split()))

n = len(numbers)

for i in range(n - 1):
    # Find the index of the largest element in the remaining list
    max_idx = i
    for j in range(i + 1, n):
        if numbers[j] > numbers[max_idx]:
            max_idx = j

    # Swap the found max value with the first unsorted position
    numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]

    # Output list after each outer loop iteration
    print([*numbers])
