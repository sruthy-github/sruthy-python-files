f=open("C:/Users/sruthy/Downloads/Temperature","r")
lst=[]
dic={}
for lines in f:
    data = lines.rstrip("\n").split(",")
    lst.append(data)
for i in lst:
    if(i[0] not in dic):
        dic[i[0]]=i[1]
    else:
        if(int(i[1])>int(dic[i[0]])):
            dic[i[0]]=i[1]
for i in dic:
    print(i, ":", dic[i])

