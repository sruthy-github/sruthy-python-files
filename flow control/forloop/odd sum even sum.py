ll = int(input("Lower limit"))
ul = int(input("Upper limit"))
oddsum = 0
evensum = 0
for i in range(ll, ul + 1):
    if (i % 2 == 0):
        evensum = evensum + i

    else:
        oddsum = oddsum + i
print("Odd Sum", oddsum)
print("Even Sum", evensum)
