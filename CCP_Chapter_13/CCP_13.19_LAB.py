# read first line
pairs = input().split()

# dictionary for contacts
contact_dict = {}

for p in pairs:
    name, phone = p.split(",")
    contact_dict[name] = phone

# read search name
search_name = input()

# output phone number
print(contact_dict[search_name])