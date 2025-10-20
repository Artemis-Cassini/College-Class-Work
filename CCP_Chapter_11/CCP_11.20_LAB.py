def feet_to_steps(num_feet):
    return int(num_feet / 2.5)

if __name__ == "__main__":
    num_feet = float(input())

    num_steps = feet_to_steps(num_feet)
    print(num_steps)