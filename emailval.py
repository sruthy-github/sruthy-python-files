import re
n=input("enter the email")
x="(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$)"
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")