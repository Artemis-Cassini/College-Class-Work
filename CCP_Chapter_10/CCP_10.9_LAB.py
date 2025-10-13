word1 = input()
word2 = input()

min_length = min(len(word1), len(word2))

match = 0
for i in range(min_length):
    if word1[i] == word2[i]:
        match += 1

if match > 1:
    print(f'{match} characters match')
if match == 1:
    print(f'{match} character matches')
if match == 0:
    print(f'{match} characters match')