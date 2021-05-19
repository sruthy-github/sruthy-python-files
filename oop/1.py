class Person:
    def print(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("inside print method\n",self.name,self.age,self.gender)
pe=Person()
pe.print("Anu",23,"female")
re=Person()
re.print("Amal",24,"male")
