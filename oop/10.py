class Employee:
    company="****Infosys****"
    def __init__(self,name,id,age,designation,salary):
        self.name=name
        self.id=id
        self.age=age
        self.designation=designation
        self.salary=salary
    def printval(self):
        print(Employee.company)
        print(self.name,self.id,self.age,self.designation,self.salary)
        print("*************")
em=Employee("Anu",15748,25,"System Engineer",35000)
em.printval()