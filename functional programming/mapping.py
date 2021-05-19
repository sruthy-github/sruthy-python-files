lst=[1,2,3,4,5,6,7,8,9,10]
s=list(map(lambda num:num*num,lst))
print(s)

lst1=[2,3,4,5,6,7]
squares=list(map(lambda num:num**2,lst1))
print(squares)


lst2=["ajay","aravind","arun"]
up=list(map(lambda name:name.upper(),lst2))
print(up)