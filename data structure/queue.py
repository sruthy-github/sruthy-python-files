lst=[]
top=0
#n=0
size=int(input("enter the size"))
def insert():
    global top,size
    if top>=size:
        print("queue is full")
    else:
        d = int(input("inputs"))


        lst.append(d)
        top+=1
        print(lst)


def delete():
    global top,size

    if(top<=0):
        print("queue is empty")
    else:
        lst.pop(0)
        top-=1
        print(lst)

while True:
    a = input("enter the operation Insert or delete")

    if (a == "insert"):
        insert()
    else:
        delete()

