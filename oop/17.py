class Person:
    def d1(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
class Parent(Person):
    def d2(self,job,salary):
        self.job=job
        self.salary=salary
        print("Parent's Job:",self.job)
        print("Parent's Salary:",self.salary)
class Child(Person):
    def d3(self,grade,school):
        self.grade=grade
        self.school=school
        print("Class:",self.grade)
        print("School:",self.school)
class Student(Child,Parent):
    def d4(self,rollno):
        self.rollno=rollno
        print("Rollno:",self.rollno)
p=Student()
p.d1("Anu",13,"F")
p.d3(7,"Toc H")
p.d4(10)
p.d2("Engineer",35000)