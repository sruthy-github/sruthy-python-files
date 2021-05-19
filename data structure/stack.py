lst=[]
top=0
n=0
size=int(input("enter the size"))
def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        d = int(input("inputs"))


        lst.append(d)
        top+=1
        print(lst)


def pop():
    global top,size

    if(top<=0):
        print("stack is empty")
    else:
        lst.pop()
        top-=1
        print(lst)

while n!=1:
    a = input("enter the operation push or pop")

    if (a == "push"):
        push()
    else:
        pop()

