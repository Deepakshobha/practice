class Bankaccount:
    def __init__(self,amount):
        self.balance = amount
        self.transaction = []
    def deposite(self,amount):
        if amount >0:
            self.balance += amount
            self.transaction.append(f'udated balance is {self.balance}')
        else:
            raise ValueError


    def withdraw(self,amount):
        if self.balance < amount:
            raise ValueError
        else:
            self.balance -= amount
            self.transaction.append(f'current balance balance is {self.balance}')


p1 = Bankaccount(0)
print(p1.deposite(1000))
print(p1.__dict__)
p1.withdraw(500)
print(p1.__dict__)
p1.withdraw(500)
print(p1.__dict__)
p1.withdraw(500)
print(p1.__dict__)
