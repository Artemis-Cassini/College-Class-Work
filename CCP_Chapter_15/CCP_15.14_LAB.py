# TODO: Declare global variables here.
recursions = 0
comparisons = 0


def binary_search(nums, target, lower, upper):
    global recursions, comparisons

    recursions += 1  # count this call

    mid = (lower + upper) // 2

    # First comparison: target == nums[mid]
    comparisons += 1
    if target == nums[mid]:
        return mid

    # Base case: not found in this 1-element range
    if lower == upper:
        return -1

    # Second comparison: nums[mid] < target (only reached if not equal)
    comparisons += 1
    if nums[mid] < target:
        # Search right half
        return binary_search(nums, target, mid + 1, upper)
    else:
        # Search left half
        return binary_search(nums, target, lower, mid - 1)
    
if __name__ == "__main__":
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input().split()]
    
    # Input a target value
    target = int(input())

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f"index: {index}, recursions: {recursions}, comparisons: {comparisons}")