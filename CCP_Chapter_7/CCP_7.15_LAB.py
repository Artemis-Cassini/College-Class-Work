highway_number = int(input())

if 1 <= highway_number <= 99:   # Primary highways
    print(f"I-{highway_number} is primary, ", end="")
    if highway_number % 2 == 0:
        print("going east/west.")
    else:
        print("going north/south.")

elif 100 <= highway_number <= 999:   # Auxiliary highways
    primary = highway_number % 100   # Last two digits
    if primary == 0:  # Not valid if ends in "00"
        print(f"{highway_number} is not a valid interstate highway number.")
    else:
        print(f"I-{highway_number} is auxiliary, serving I-{primary}, ", end="")
        if primary % 2 == 0:
            print("going east/west.")
        else:
            print("going north/south.")

else:
    print(f"{highway_number} is not a valid interstate highway number.")