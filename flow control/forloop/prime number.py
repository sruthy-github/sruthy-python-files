num=int(input("Enter number"))
temp=0
for i in range(2,num):
    if(num%i==0):
        temp=1

if(temp==1):
    print(num,"Not prime")
else:
    print(num,"Prime")
