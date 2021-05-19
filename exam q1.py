lst=[1,2,3,3,4,3,5,5,7]
dup=[]
for i in lst:
    if i not in dup:
        dup.append(i)
print(lst)
print(dup)
