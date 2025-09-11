phone_number = int(input())

# extract parts
line_number = phone_number % 10000
prefix = (phone_number // 10000) % 1000
area_code = phone_number // 10000000

# format with leading zeros where needed
print(f"({area_code:03d}) {prefix:03d}-{line_number:04d}")