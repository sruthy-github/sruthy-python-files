class Person:
    company="****INFOSYS****"
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdetails(self):
        print(Person.company)
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):
    def det(self,salary,designation):
        self.salary=salary
        self.designation=designation
    def print(self):
        print(self.salary)
        print(self.designation)
        print("***************")
p=Employee()
p.details("Anu",25,"F")
p.printdetails()
p.det(35000,"System Engineer")
p.print()
