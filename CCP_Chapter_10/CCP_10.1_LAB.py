user_text = input()

exclude_characters = " .,!"

count = sum(1 for char in user_text if char not in exclude_characters)

print(count)
