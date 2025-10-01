strokes = int(input())
par = int(input())

result = "Error"

if par in [3, 4, 5]:
    if strokes == par - 2:
        result = "Eagle"
    elif strokes == par - 1:
        result = "Birdie"
    elif strokes == par:
        result = "Par"
    elif strokes == par + 1:
        result = "Bogey"

print(f"Par {par} in {strokes} strokes is {result}")