# Description of the game
print("Enter coins required to make exactly one dollar \n")

# Prompting user for inputs of coins
quarters = int(input("Enter number of quarters: "))
dimes = int(input("Enter number of dimes: "))
nickels = int(input("Enter number of nickels: "))
pennies = int(input("Enter number of pennies: "))

# Finding total cents by adding // multiplying coin values
total_cents = quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1

# Convert the cents to dollars
total_dollars = total_cents / 100

# Output result
# print(f"Total amount: ${total_dollars:.2f}") # I added this in but I have it so it doesn't 
# show so the player doesn't know the amount they entered

if total_dollars == 1:
    print("Congrats player, you win!") # If the player wins
elif total_dollars > 1:
    print("You are over") # If player is over
else:
    print("You are under") # If player is under
