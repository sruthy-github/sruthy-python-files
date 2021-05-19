line="hai hello hai hello good morning everyone"
words=line.split(" ")
print(words)
dic={}
for i in words:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1


print(dic)