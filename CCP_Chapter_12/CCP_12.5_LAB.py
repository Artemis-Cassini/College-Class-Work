def calc_toll(hour, is_morning, is_weekend):
    if is_weekend:
        # Weekend tolls
        if is_morning:
            if hour < 7:
                return 6.05
            else:
                return 7.15
        else:
            if hour < 8:
                return 7.15
            else:
                return 6.10
    else:
        # Weekday tolls
        if is_morning:
            if hour < 7:
                return 6.15
            elif hour < 10:
                return 7.95
            else:
                return 6.90
        else:
            if hour < 3:
                return 6.90
            elif hour < 8:
                return 8.95
            else:
                return 6.40


if __name__ == "__main__":
    print(calc_toll(8, True, False))   # 7.95 ✅
    print(calc_toll(1, False, False))  # 6.90 ✅
    print(calc_toll(3, False, True))   # 7.15 ✅
    print(calc_toll(5, True, True))    # 6.05 ✅