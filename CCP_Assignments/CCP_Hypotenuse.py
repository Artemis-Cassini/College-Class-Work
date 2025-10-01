#Purpose: This program finds the length of the hypotenuse of a right triangle
# when given the lengths of the other two sides.
import math
#Prompt user for lengths of the two sides(a and b)
a = float(input("Enter length of a: \n"))
b = float(input("Enter length of b: \n"))
#Calculate the hypotenuse
c = math.sqrt(a**2 + b**2)
#Print the length of the hypotenuse with 2 digits after the decimal point
print(f'Length of hypotenuse is: {c:.2f}')


# I'm using a pythagorean triple as my input (69, 260, 269)
