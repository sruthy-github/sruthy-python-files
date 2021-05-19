class Person:
    def setval(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
pe=Person()
pe.setval("Anu",23)
pe.printval()