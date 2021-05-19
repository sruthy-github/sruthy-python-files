class Vehicle:
    def print(self,name,nooftyre):
        self.name=name
        self.nooftyre=nooftyre
        print("THE VEHICLES ARE\n  ",self.name,self.nooftyre)
v=Vehicle()
v.print("Car",4)
a=Vehicle()
a.print("Bus",6)
