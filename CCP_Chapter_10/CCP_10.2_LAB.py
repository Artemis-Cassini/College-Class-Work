number = int(input())

while 11 <= number <= 99:
    print(number, end='\n')
    if number % 11 == 0:
        break
    number -= 1

else:
    print("Input must be 11-99")