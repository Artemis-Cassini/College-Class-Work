def get_user_values():
    num_values = int(input())
    user_values = [int(input()) for _ in range(num_values)]
    upper_threshold = int(input())
    return user_values, upper_threshold

def ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    return [value for value in user_values if value <= upper_threshold]

if __name__ == "__main__":
    user_values, upper_threshold = get_user_values()
    res_values = ints_less_than_or_equal_to_threshold(user_values,
                                                      upper_threshold)

    for value in res_values:
        print(value)