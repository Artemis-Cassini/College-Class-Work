  # Importing random to select a target amount
import random

# User-defined functions here
def generate_target_amount(min_cents=1, max_cents=100):
    return random.randint(min_cents, max_cents)

def compute_total_cents(quarters, dimes, nickels, pennies):
    return quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1  # Passes

def format_dollars(cents):
    return f"${cents/100:.2f}"

def compare_amount(user_cents, target_cents):
    if user_cents < target_cents:
        return "low"
    elif user_cents > target_cents:
        return "high"
    else:
        return "correct"

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

    # Finding total cents by adding // multiplying coin values
    # total_cents = quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1
    total_cents = compute_total_cents(quarters, dimes, nickels, pennies)

    # Convert the cents to dollars
    total_dollars = total_cents / 100

    # Show the user's amount every attempt
    print(f"Your amount: {format_dollars(total_cents)}")

    # Output result
    # print(f"Total amount: ${total_dollars:.2f}") # I added this in but I have it so it doesn't 
    # show so the player doesn't know the amount they entered

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
        # Continue the loop automatically until player is correct
        continue
    else:
        print("You are under")
        # Continue the loop automatically until player is correct
        continue
