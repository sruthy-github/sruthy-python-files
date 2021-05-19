f=open("numbers","r")
lst=[]
sum=0
for numbers in f:
    lst.append(int(numbers))
print(lst)
for i in lst:
    sum=sum+i
print(sum)
