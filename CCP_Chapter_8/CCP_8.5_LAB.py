# Write a program that reads two phrases on separate lines and outputs one of four responses:

# 1) Phrase one is found within phrase two
# 2) Phrase two is found within phrase one
# 3) Both phrases match
# 4) No matches

# Hint: Use membership operator in.

phrase_one = str(input())
phrase_two = str(input())

if phrase_one == phrase_two:
    print("Both phrases match")
elif phrase_one in phrase_two:
    print(phrase_one, "is found within", phrase_two)
elif phrase_two in phrase_one:
    print(phrase_two, "is found within", phrase_one)

else:
    print("No matches")
