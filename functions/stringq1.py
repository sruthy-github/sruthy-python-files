a="Hello World"
b=input("Enter letter")
flag=1
for st in a:
    if(st==b):
        flag=0

if(flag==0):
    print("Present")
else:
    print("Not Present")