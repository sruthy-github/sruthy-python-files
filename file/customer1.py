f=open("C:/Users/sruthy/OneDrive/Desktop/customer","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    fname=data[1]
    age=data[3]
    cou=data[-1]
    temp=([fname,age,cou])
    if(temp[2]=="india"):
        print(temp)


