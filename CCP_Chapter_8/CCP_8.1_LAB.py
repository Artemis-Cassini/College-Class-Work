# input is 130, 50, 130

red = int(input())
green = int(input())
blue = int(input())


colors = [red, green, blue]
smallest = min(colors)

final = red - smallest
final2 = green - smallest
final3 = blue - smallest

print(final, final2, final3)
