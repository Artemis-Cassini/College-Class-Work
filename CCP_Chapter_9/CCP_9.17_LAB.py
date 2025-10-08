user_input = input()

while user_input not in ("Done", "done", "d"):
    print(user_input[::-1])
    user_input = input()