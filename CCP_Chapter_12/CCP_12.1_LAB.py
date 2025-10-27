def laps_to_miles(user_laps):
    user_miles = user_laps*0.25
    return user_miles

if __name__ == "__main__":
    user_laps = float(input())
    print(f'{laps_to_miles(user_laps):.2f}')
