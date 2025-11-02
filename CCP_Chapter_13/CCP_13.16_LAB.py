numbers = input().split()
    
numbers = [float(num) for num in numbers if float(num) >= 0]
    
if numbers:
    max_value = max(numbers)
    average = sum(numbers) / len(numbers)
        
    print(f"{max_value:.2f} {average:.2f}")
else:
    print()
