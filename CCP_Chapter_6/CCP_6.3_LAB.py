# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
favorite_color = input("Enter favorite color:\n")
pet_name = input("Enter pet name:\n")
number = input ("Enter a number:\n")

print("You entered:", favorite_color, pet_name, number)

# ---------------------------------------------------------------------------------

# FIXME (2): Output two password options
password1 = favorite_color + "_" + pet_name
password2 = number + favorite_color + number
print(f"\nFirst password: {password1}")
print(f"Second password: {password2}")

# ---------------------------------------------------------------------------------

# FIXME (3): Output the length of the two password options
print(f"\nNumber of characters in ", password1, ": ", len(password1), sep="")
print(f"Number of characters in ", password2, ": ", len(password2), sep="")

# ---------------------------------------------------------------------------------

# input 1 is yellow Daisy 6
# output should be "You entered: yellow Daisy 6"

# same input
# output will be.. (You entered: yellow Daisy 6) // First password: yellow_Daisy // Second password: 6yellow6

# same input
# output will be.. (You entered: yellow Daisy 6 // First password: yellow_Daisy // Second password: 6yellow6)
# (con) Number of characters in yellow_Daisy: 12 // Number of characters in 6yellow6: 8
# print(f"Length: {len(password2)}") do something like this??



