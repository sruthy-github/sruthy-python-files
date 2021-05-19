class Calculator:
    num1=int(input("Enter num1"))
    num2=int(input("Enter num2"))
    def add(self):
        print("********")
        print("Result:",self.num1+self.num2)
    def sub(self):
        print("********")
        print("Result:",self.num1-self.num2)
    def mul(self):
        print("********")
        print("Result:",self.num1*self.num2)
    def div(self):
        print("********")
        print("Result:",self.num1/self.num2)
p=Calculator()
p.add()
p.sub()
p.mul()
p.div()
