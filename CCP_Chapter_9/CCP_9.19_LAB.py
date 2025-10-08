user_num = int(input())

num_list = []

for i in range(user_num):
    num_list.append(float(input()))

max_num = max(num_list)

for num in num_list:
    num_result = num / max_num
    print(f'{num_result:.2f}')