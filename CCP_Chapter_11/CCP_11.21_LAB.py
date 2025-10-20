def int_to_reverse_binary(integer_value):
    binary_str = ''
    while integer_value > 0:
        binary_str += str(integer_value % 2)
        integer_value = integer_value //2
    return binary_str

def string_reverse(input_string):
    return input_string[::-1]

if __name__ == "__main__":
    integer_value = int(input())
    reversed_binary = int_to_reverse_binary(integer_value)
    binary = string_reverse(reversed_binary)
    print(binary)
