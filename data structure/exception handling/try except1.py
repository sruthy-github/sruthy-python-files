lst=[1,2,3,4,5,6]
i=int(input("index"))
try:
    print(lst[i])
except:
    print("exception occured")
finally:
    print("inside finally")