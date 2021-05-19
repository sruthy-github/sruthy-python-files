import functools
lst=[7,8,9,4,3,2]
total=functools.reduce(lambda no1,no2:no1+no2,lst)
print(total)
