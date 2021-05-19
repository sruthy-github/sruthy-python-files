class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("********")
        print("Name:",self.name)
        print("Age:",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print("Rollno:",self.rollno)
        print("Mark:",self.mark)
        print("********")
p=Student(3,47,"Anu",13)
p.printval()
p.print()