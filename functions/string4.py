a=input("Enter string")
b=input("Enter letter")
count=0
for i in a:
    if(i==b):
        if(b=="a","e","i","o","u"):
            count+=1
print(count)