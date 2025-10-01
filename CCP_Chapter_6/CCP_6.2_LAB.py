current_price = int(input())
last_months_price = int(input())

# calculate difference
change = current_price - last_months_price

# monthly mortgage estimate
your_value = (current_price * 0.051) / 12

# print result
print(f"This house is ${current_price}. The change is ${change} since last month.")
print(f"The estimated monthly mortgage is ${your_value:.2f}.")