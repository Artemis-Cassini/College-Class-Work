# Define your get_user_values function here
def get_user_values(nums):
    val = int(input())
    while val != -1:
        nums.append(val)
        val = int(input())

# Define your output_ints_less_than_or_equal_to_threshold function here
def output_ints_less_than_or_equal_to_threshold(nums, threshold):
    for n in nums:
        if n <= threshold:
            print(n)


if __name__ == "__main__":
    threshold = int(input())
    nums = []

    get_user_values(nums)
    output_ints_less_than_or_equal_to_threshold(nums, threshold)