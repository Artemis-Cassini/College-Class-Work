# Importing random to select a target amount
import random

# Dictionary that stores coin names and values in cents
# The purpose of this allows flexible use of coin value lookups
# Passed to: compute_total_cents_from_dict()
COIN_VALUES = {
    "quarters": 25,
    "dimes": 10,
    "nickels": 5,
    "pennies": 1
}

# User-defined functions here

# The purpose of this is to generate a return a random integer number 
# of cents that is within the max and min range.
# Parameters - min_cents - lowest random value allowed // max_cents - highest random value allowed
# This will return the integer amount of cents randomly chosen
def generate_target_amount(min_cents=1, max_cents=100):
    return random.randint(min_cents, max_cents)

# The purpose of this is to calculate and return the total cents based
# on what the user puts in
# Parameters - quaters, dimes, nickels, pennies - integers that show each number of coin type entered by the user
# This will return the integer total number of cents
def compute_total_cents(quarters, dimes, nickels, pennies):
    return quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1

# The purpose of this is to convert the cents value to a string
# formatted in dollars w/ 2 decimal places
# Parameters - cents - integer number of cents
# This will return the string in the format "$X.XX"
def format_dollars(cents):
    return f"${cents/100:.2f}"

# The purpose of this is to comapre the user's total cents with the hidden target cents
# then indicate if it's low, high, or correct
# Parameters - user_cents - integer representing the user's total amount
# cont. target_cents - integer representing the target amount
# This will return the string of low, high, or correct
def compare_amount(user_cents, target_cents):
    if user_cents < target_cents:
        return "low"
    elif user_cents > target_cents:
        return "high"
    else:
        return "correct"

# The purpose of this is to calculate the total value
# of coins using a dictionary of coin counts
# Parameters - coin_counts - a dictionary mapping coin names to their counts (quarters, dimes, nickels, pennies)
# cont. coin_values - a dictionary mapping coin names to their values in cents (COIN_VALUES
# This will then return the integer total number of cents
def compute_total_cents_from_dict(coin_counts, coin_values=COIN_VALUES):
    total = 0
    for coin, count in coin_counts.items():
        total += count * coin_values[coin]
    return total

# Description of the game
print("Enter coins required to make exactly one dollar \n")

# Hidden target so player must guess
target_cents = generate_target_amount(1, 100)  

# Add loop
while True:
    # Prompting user for inputs of coins
    quarters = int(input("Enter number of quarters: "))
    dimes = int(input("Enter number of dimes: "))
    nickels = int(input("Enter number of nickels: "))
    pennies = int(input("Enter number of pennies: "))

    # Dictionary storing coin counts to use with dictionary-based computation
    coin_counts = {
        "quarters": quarters,
        "dimes": dimes,
        "nickels": nickels,
        "pennies": pennies,
    }

    # Finding total cents using dictionary method
    total_cents = compute_total_cents_from_dict(coin_counts)

    # Convert the cents to dollars
    total_dollars = total_cents / 100

    # Show the user's amount every attempt
    print(f"Your amount: {format_dollars(total_cents)}")

    # Output result
    result = compare_amount(total_cents, target_cents)
    if result == "correct":
        print("Congrats player, you win!")

        # Ask player if they want to play again 
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again in ["y", "yes"]:
            target_cents = generate_target_amount(1, 100) # If yes, new hidden target
            continue
        else:
            print("Thanks for playing!")
            break

    elif result == "high":
        print("You are over")
        continue

    else:
        print("You are under")
        continue
