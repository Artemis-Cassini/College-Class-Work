import random

def coin_flip():
    if random.randint(0,1) == 1:
        return "Heads"
    else:
        return "Tails"

if __name__ == "__main__":
    random.seed(5)  # Unique seed
    number_of_flips = int(input())

    for _ in range(number_of_flips):
        print(coin_flip())
