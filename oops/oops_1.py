# class bankaccount:
#     interest_rate= 0.04 #class varialbe
#     #common to all
#     def __init__(self,name,balance=0): #self = variable name convention self
#         self.name = name
#         self.balance = balance # if balance value not provided by default balnce is zero
#         self.transaction = [] # to maintain details and track
#         self.transaction.append(f"******* intial deposited {balance} ****")
#     def deposite(self,amount):
#         self.balance = self.balance + amount
#         self.transaction.append(f"ammount deposited{amount}")
#
#     def withdraw(self,amount ):
#         if amount > self.balance:
#             raise ValueError('Insufficient fund')
#         self.balance = self.balance-amount
#         self.transaction.append(f"amount withdraw {amount}")
#         return f"please collect the cashe {amount}"
#     def transfer(self,to_account,amount):
#         if self.balance <= amount:
#             raise ValueError ("insufficient fund")
#         to_account.deposite(amount)
#         self.balance -= amount
#
#     def statement(self, amount=None):
#         for transaction in self.transaction:
#             print(transaction)
#         print('*'*20)
#         return f"please collect the cashe {amount}"
#     def roi(self):
#         interest_amount = self.balance * bankaccount.interest_rate
#         self.balance += interest_amount
#         self.transaction.append(f"{interest_amount} credite")
# c1 = bankaccount('shobha',1000)
# c2 = bankaccount('xyz',2000)
# c3 = bankaccount('pqr',4000)
# print(c1.deposite(10000))
# print(c1.transfer(c3,3000))
# print(c1.withdraw(600))
# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)
# # for transcation in c1.transaction:
# #     print(transcation)
# # print(c1.statement())
# c1.roi()
# print(c1.balance)
# print(c1.__class__)
# print(bankaccount.interest_rate)
# # print(c1.__class__.__dict__)

# incrementing class variables #we can write how many people login
# class demo:
#     # shared across all the instances
#     count = 0
#     def __init__(self,a,b):
#         self.a = 1
#         self.b = 1
#         demo.count =demo.count+1
# d1 =demo(1,2)
# print(demo.count)
# d2 = demo(3,4)
# print(demo.count)
# d2 = demo(3,4)
# print(demo.count)
# print(demo.__dict__)
# print(d1.__dict__)
# #
#
#
#
class Demo:
    count = 0
    def __int__(self,a,b):
        self.a = 1
        self.b = 1
        Demo.count = Demo.count + 1

d1 =Demo()
print(.count)
print(.count)








