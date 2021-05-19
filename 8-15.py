import re
n=input("Enter the string")
x="([\D]{8,15}$)"
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")