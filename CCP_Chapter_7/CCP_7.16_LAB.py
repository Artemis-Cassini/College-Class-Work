month = input().strip().lower()
day = int(input())

# Map month names to numbers and their max days
months = {
    "january": (1, 31), "february": (2, 29), "march": (3, 31),
    "april": (4, 30), "may": (5, 31), "june": (6, 30),
    "july": (7, 31), "august": (8, 31), "september": (9, 30),
    "october": (10, 31), "november": (11, 30), "december": (12, 31)
}

if month not in months:
    print("Invalid")
else:
    m, max_day = months[month]
    if day < 1 or day > max_day:
        print("Invalid")
    else:
        if (m == 3 and day >= 20) or (m in [4, 5]) or (m == 6 and day <= 20):
            season = "Spring"
        elif (m == 6 and day >= 21) or (m in [7, 8]) or (m == 9 and day <= 21):
            season = "Summer"
        elif (m == 9 and day >= 22) or (m in [10, 11]) or (m == 12 and day <= 20):
            season = "Autumn"
        else:
            season = "Winter"

        print(season)