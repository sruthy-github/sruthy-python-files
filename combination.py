import re
n=input("Enter the string")
x="(^[A-Z][a-z]$)"
match=re.finditer(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")
