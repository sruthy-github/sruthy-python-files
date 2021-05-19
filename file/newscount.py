f=open("newsread","r")
words=[]
for i in f:
    words.append(i.rstrip("\n"))
fil=words.split(" ")
dic={}
for i in fil:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic[i])   