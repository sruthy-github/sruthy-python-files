class Parent:
    def m1(self):
        print("Parent Class")
class Child(Parent):
    def m2(self):
        print("Child Class")
class Subchild(Child):
    def m3(self):
        print("Subchild Class")
obj=Subchild()
obj.m1()
obj.m2()
obj.m3()