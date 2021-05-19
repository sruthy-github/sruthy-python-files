class Employee:
    company="****INFOSYS****"
    def setval(self,name,id,designation,salary):
        self.name=name
        self.id=id
        self.designation=designation
        self.salary=salary
        #self.company=company
    def printval(self):
        print(Employee.company)
        print("Name:",self.name)
        print("Company id:",self.id)
        print("Designation:",self.designation)
        print("Salary:",self.salary)
        print("**************")

em=Employee()
em.setval("Anu",101235,"System Engineer",35000)
em.printval()
