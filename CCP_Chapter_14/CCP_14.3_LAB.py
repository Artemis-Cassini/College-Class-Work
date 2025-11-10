def calc_average(nums):
    average = sum(nums) / len(nums)
    return int(average)
    
if __name__ == "__main__":
    nums = [1.1, 2.1, 3.1, 4.1, 5.1]
    print(calc_average(nums))   # calc_average() should return 3