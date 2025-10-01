# input is night // 50
# input is day // 15
# input is night // 3

# Movie prices are free for everyone under the age of 4. Daytime prices are $8 for everyone age 4 or higher. 
# Nighttime prices are $12 for ages 4 - 16, $15 for ages 17 - 54 and $13 for ages 55 and above.

# Take inputs
time_of_day = input()   # expects "day" or "night"
age = int(input())

# Decide price
if age < 4:
    print("free")
else:
    if time_of_day == "day":
        print("$8")
    elif time_of_day == "night":
        if 4 <= age <= 16:
            print("$12")
        elif 17 <= age <= 54:
            print("$15")
        else:  # age >= 55
            print("$13")