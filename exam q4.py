a=int(input("enter the limit"))
n1=0
n2=1
x=0
count=1
while count<=a:
    print(x)
    count += 1
    n1=n2
    n2=x
    x = n1 + n2
