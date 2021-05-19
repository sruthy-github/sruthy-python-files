lst1=[7,8,9,4,3,1]
lst=[]
for i in lst1:

        lst.append(i+1) if i>5 else  lst.append(i-1)
print(lst)
