lst=[]
odd=[]
even=[]
for i in range(1,101):
    lst.append(i)
for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print('list:',lst)
print('odd:',odd)
print('even:',even)