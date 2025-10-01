# input is 35 and 45

speed_limit = int(input())
driving_speed = int(input())

difference = driving_speed - speed_limit

if difference <= -10:
    print("50")
elif 6 <= difference <= 20:
    print("75")
elif 21 <= difference <=40:
    print("150")
elif difference >= 40:
    print("300")
else:
    print("0")
