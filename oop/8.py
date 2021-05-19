class Bank:
    name="Canara bank"
    def creation(self,number,balance):
        self.minimumbalance=5000
        self.number=number
        self.balance=balance
        self.balance=self.minimumbalance
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        print("Amount Available:",self.balance)
    def withdraw(self,wamount):
        self.wamount=wamount
        self.balance-=self,wamount
        print("Amount available:",self.balance)


a=Bank()

a.creation(1235,2000)
a.deposit(1000)
