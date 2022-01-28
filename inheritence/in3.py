class bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        if amount < 0:
            raise ValueError('Amount should be greater than zero')
        self.balance += amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            raise ValueError('insufficinent fund')

    def roi(self):
        intrest_amount = self.balance * self.__class__.interest_rate
        self.balance +=  intrest_amount


class Sbaccount(bankaccount):
    interest_amount =0.05
    def withdraw(self, amount):
        if amount > 10000:
            raise ValueError ("cannot withdraw more than 10k")  #adding extra functionality
        super().withdraw(amount) #not changing original function

class salaryaccount(bankaccount):
    def __init__(self,name):
        self.is_first_monthsalary =True
        self.max_draft_amount = 10000
        self.draft_amountn = 0.0
        super().__init__(name,0.00)
    # else:
    #     raise ValueError(f"max available draft {self.max_draft_amount}")

    def deposite(self, amount):
        if self.is_first_monthsalary:
            self.is_first_monthsalary = False
            super().deposite(amount+1000)
        else:
            super.deposite(amount)

    def overdraft(self,amount):
        if self.draft_amount+amount<=self.max_draft_amount:
            super().deposite(amount) #handover the amount to deposite method of parent class
            self.max_draft_amount -= amount

class sukanyasamrudhiaccount(bankaccount):
    iterest_rate = 0.03
    def __init__(self,name,balance):
        if balance <1000:
            raise ValueError()
        super().__init__(name,balance)
    def deposite(selfself,amount):
        if amount <1000:
            raise ValueError('min amount to deposite is 1k')
        super().deposite(amount)

    def withdraw(self,amount):
        raise Exception("you can draw amount from ")
d = salaryaccount('steve')
print(d.__dict__)

# s1.__dict__
# # s1.overdraft(1000)
# s2.overdrfat(2000)

# class Demo:
#     a = 10
#     def demo(self):
#         print("demo",self.__class__.a)
#
# class child(Demo):
#     a = 100
#     # def demo(self):
#     #     print('child demo')
#
# c= child()
# c.demo()
s=Sbaccount("steve",20000)

s.deposite(20000)
# print(s.__dict__)
# s.withdraw(15000)
# print(s.__dict__)
print(d.__dict__)
print(s.__dict__)
print(d.__dict__)