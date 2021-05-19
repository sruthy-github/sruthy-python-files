class Person:
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name,self.age,self.gender)
pe=Person()
pe.setval("Anu",23,"F")
pe.printval()