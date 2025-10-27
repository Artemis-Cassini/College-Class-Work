def exact_change(input_val):

    num_quarters = input_val // 25
    input_val %= 25

    num_dimes = input_val // 10
    input_val %= 10

    num_nickels = input_val // 5
    input_val %= 5

    num_pennies = input_val
    return num_pennies, num_nickels, num_dimes, num_quarters

if __name__ == "__main__":
    input_val = int(input())
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)
    if input_val <= 0:
        print("no change")
    else:
        if num_pennies > 0:
            if num_pennies == 1:
                print(f'{num_pennies} penny')
            else:
                print(f'{num_pennies} pennies')
        if num_nickels > 0:
            if num_nickels == 1:
                print(f'{num_nickels} nickel')
            else:
                print(f'{num_nickels} nickels')
        if num_dimes > 0:
            if num_dimes == 1:
                print(f'{num_dimes} dime')
            else:
                print(f'{num_dimes} dimes')
        if num_quarters > 0:
            if num_quarters == 1:
                print(f'{num_quarters} quarter')
            else:
                print(f'{num_quarters} quarters')