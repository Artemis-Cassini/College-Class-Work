total_change = int(input())

if total_change == 0:
    print("No change")

else:
    dollars = total_change // 100
    total_change %= 100

    quarters = total_change // 25
    total_change %= 25

    dimes = total_change // 10
    total_change %= 10

    nickels = total_change // 5
    total_change %= 5

    pennies = total_change

    def print_coin(count, singular, plural):
        if count == 1:
            print(f"{count} {singular}")
        elif count > 1:
            print(f"{count} {plural}")

    print_coin(dollars, "Dollar", "Dollars")
    print_coin(quarters, "Quarter", "Quarters")
    print_coin(dimes, "Dime", "Dimes")
    print_coin(nickels, "Nickel", "Nickels")
    print_coin(pennies, "Penny", "Pennies")
