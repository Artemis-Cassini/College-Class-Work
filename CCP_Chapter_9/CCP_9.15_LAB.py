word = input()
password = ""

word = word.replace('i', '1')
word = word.replace('a', '@')
word = word.replace('m', 'M')
word = word.replace('B', '8')
word = word.replace('s', '$')

word = word + '!'
print(word)