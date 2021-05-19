lst1=[10,20,21,22,23]
lst2=[20,21,10,22,23]
lst1.sort()
lst2.sort()
if lst1.sort()==lst2.sort():
    print("Identical")
else:
    print("Not Identical")