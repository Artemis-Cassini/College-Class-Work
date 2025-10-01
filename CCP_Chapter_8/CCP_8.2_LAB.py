string1 = input()
string2 = input()

if len(string1) > len(string2):
    print(string1, "is longer than", string2)
elif len(string1) < len(string2):
    print(string2, "is longer than", string1)
else:
    print(string1, "and", string2, "are the same length")