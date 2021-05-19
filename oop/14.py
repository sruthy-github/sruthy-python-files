class Numbers():
    def m1(self):
        print("Its a collection of numbers")
        print("********")
class PositiveNumber():
    def m2(self):
        print("Collection of Positive Numbers")
class Fraction(PositiveNumber,Numbers):
    def m3(self):
        print("********")
        print("Collection of Fractions")
obj=Fraction()
obj.m3()
obj.m2()
obj.m1()