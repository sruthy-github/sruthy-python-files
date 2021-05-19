s=input("Enter string")
a=""
for i in s:
    if(i!="!@#$%^&*():;{}[]|\+=<>?/,."):
        a=s+i
print(a)
