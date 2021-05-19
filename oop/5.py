class Addition:
    def setval(self,digit1,digit2):
        self.digit1=digit1
        self.digit2=digit2
    def operation(self):
        print("The sum is:")
        print(self.digit1+self.digit2)
sum=Addition()
sum.setval(10,20)
sum.operation()