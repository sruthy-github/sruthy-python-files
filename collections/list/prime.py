lst=[]
prime=[]
for i in range(1,101):
    lst.extend([i])
for i in lst:
    for j in range(2,i):

        if (i%j==0):
            break

    else:
        prime.append(i)
prime.remove(1)
print(prime)



