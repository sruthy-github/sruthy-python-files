import functools
lst=[7,8,9,4,3,2]
largest=functools.reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(largest)