#lst=[]
#for i in range(1,51):
#    lst.append(i)
#print(lst)
lst=[i for i in range(1,51)]
print(lst)
lst1=[i for i in range(1,51) if i%2==0]
print(lst1)
lst2=[i*i if i%2==0 else i*i*i for i in range(1,51)]
print(lst2)
lst3=["even" if i%2==0 else "odd" for i in range(1,51)]
print(lst3)