class Shape:
    def m1(self):
        print("Shape")
class Polygon(Shape):
    def m2(self):
        print("Polygon")
class Square(Polygon):
    def m3(self):
        print("Square")
        print("********")
obj=Square()
obj.m1()
obj.m2()
obj.m3()
obj2=Polygon()
obj2.m1()
obj2.m2()