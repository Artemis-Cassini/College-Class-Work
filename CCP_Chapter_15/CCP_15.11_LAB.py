# Global variable
num_calls = 0

# TODO: Write the partitioning algorithm - pick the middle element as the 
#       pivot, compare the values using two index variables l and h (low and high), 
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    # Choose middle element as pivot
    pivot_index = (i + k) // 2
    pivot = user_ids[pivot_index]

    l = i        # low index
    h = k        # high index
    done = False

    while not done:
        # Move l right while element < pivot
        while user_ids[l] < pivot:
            l += 1

        # Move h left while element > pivot
        while pivot < user_ids[h]:
            h -= 1

        # If indices cross, partition is done
        if l >= h:
            done = True
        else:
            # Swap elements at l and h
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp

            l += 1
            h -= 1

    # h is the split point
    return h

# TODO: Write the quicksort algorithm that recursively sorts the low and 
#       high partitions. Add 1 to num_calls each time quicksort() is called
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i >= k:
        return

    # Partition the list and get the split index
    j = partition(user_ids, i, k)

    # Recursively sort left and right partitions
    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
        
    # Initial call to quicksort 
    quicksort(user_ids, 0, len(user_ids) - 1)
    
    # Print number of calls to quicksort
    print(num_calls)
    
    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)