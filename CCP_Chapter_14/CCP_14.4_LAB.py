def remove_odds(nums):
    odd = []
    for i in nums:
        if i % 2 == 0:
            odd.append(i)
    return odd
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = remove_odds(nums)
    
    print(result)