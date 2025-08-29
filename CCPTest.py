#area_code = input()
#prefix = input()
#line_number= input()

#string = "country code/area code/prefix/line number"
#my_tokens = string.split("/")

#print("Country  Phone Number")
#print("-------  ------------")
#print("U.S.     +1 ", "(",area_code,")",prefix,'-',line_number)

# take full input as one string
raw_input = input()

# split the string into parts
area_code, prefix, line_number = raw_input.split()

prefixNum = int(prefix)

# header
print("Country  Phone Number")
print("-------  ------------")

# formatted output
print(f"U.S.     +1 ({area_code}){prefix}-{line_number}")
print(f"Brazil   +55 ({area_code}){prefixNum + 100}-{line_number}")