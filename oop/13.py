class Parent():
    def m1(self):
        print("********")
        print("inside parent class")
class Child(Parent):
    def m2(self):
        print("inside child class")
class Subchild(Child,Parent):
    def m3(self):
        print("inside subchild class")
        print("********")
obj=Subchild()
obj.m3()
obj.m2()
obj.m1()