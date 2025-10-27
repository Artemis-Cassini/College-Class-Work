def days_in_feb(user_year):
    leap = 4
    leap_feb = 29
    reg_feb = 28
    if (user_year % leap == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        print(f'{user_year} has {leap_feb} days in February.')
        return leap_feb    #must return it by difference in the two so leap year if it is a leap year and regualr if it isnt a leap year as in else statment
    else:
        print(f'{user_year} has {reg_feb} days in February.')
        return reg_feb

if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    user_year = int(input())
    days_in_feb(user_year)