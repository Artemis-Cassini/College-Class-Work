# Dictionary of services and their costs
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12
}

# (1) Output the menu
print("Davy's auto shop services")
for service, cost in services.items():
    print(f"{service} -- ${cost}")

# (2) Prompt for two services
service1 = input("\nSelect first service:\n")
service2 = input("Select second service:\n")

# (3 & 4) Output invoice
print("\nDavy's auto shop invoice\n")

# Handle first service
if service1 == "-":
    print("Service 1: No service")
    cost1 = 0
else:
    cost1 = services[service1]
    print(f"Service 1: {service1}, ${cost1}")

# Handle second service
if service2 == "-":
    print("Service 2: No service")
    cost2 = 0
else:
    cost2 = services[service2]
    print(f"Service 2: {service2}, ${cost2}")

# Total
print(f"\nTotal: ${cost1 + cost2}")