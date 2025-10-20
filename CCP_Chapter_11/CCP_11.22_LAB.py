def swap_values(val1, val2, val3, val4):
    return val2, val1, val4, val3

if __name__ == '__main__':
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    val4 = int(input())

    swapped_vals = swap_values(val1, val2, val3, val4)
    print(f'{swapped_vals[0]} {swapped_vals[1]} {swapped_vals[2]} {swapped_vals[3]}') 