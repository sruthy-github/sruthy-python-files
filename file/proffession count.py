f=open("C:/Users/sruthy/OneDrive/Desktop/customer","r")
count={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    pro=data[4]
    for i in data:
        if pro not in count:
            count[pro]=1
        else:
            count[pro]+=1
print( count)

