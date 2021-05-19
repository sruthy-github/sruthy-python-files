import re
n=input("ener the num to validate")
x='\W{1}\d{10}$'
match=re.finditer(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")