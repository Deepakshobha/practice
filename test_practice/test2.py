# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#
#     def email(self):
#         return f'{self.fname}.{self.lname}@company.com'
#
# e1 = Employee("Steve", "Jobs", 1000)
# e2 = Employee("Bill", "Gates", 2000)
#
# print(e1.__dict__)
# print(e1.email())
#
#
# class Employee:
#     def __init__(self, fname, lname, pay,*args):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#         self.args = args
#
# e1 = Employee('steve', 'jobs', 1000, 'python', 26, '2200 valley view lane')
# print(e1.__dict__)
#
#
#
# class Users:
#     def __init__(self, users="sho"):
#         self._users = [ ]
#         if users:
#             for user in users:
#                 self._users.append(user)
#
#     def append(self, username):
#         self._users.append(username)
#
# c1 = Users()
# print(c1.__dict__)
# c1.append("shobha")
# print(c1.__dict__)

#inheritence
# class Parent:
#     def __init__(self, value):
#         self.value = value
#
#     def apple(self):
#         print('Parent.Apple', self.value)
#
#     def google(self):
#         print('Parent.Google')
#         self.apple()
#
# # c1 = Parent(20)
# # print(c1.__dict__)
# # c1.apple()
# # c1.google()
#
# class Child1(Parent):
#     def yahoo(self):
#         print('Child1 Yahoo')
#
# class Child2(Parent):
#     def apple(self):
#         print('Child2 Yahoo')
#
# class Child3(Parent):
#     def apple(self):
#         print('Child3 Yahoo')
#         super().apple()
#
# class Child4(Parent):
#     def __init__(self, value, extra):
#         self.extra_value = extra
#         super().__init__(value)



# c2 = Child4(1,2)
# c2.__init__(10,20)
# print(c2.__dict__)

# class Spam:
#     a = 10
#     def apple(self):
#         print('apple', self.__class__.a)
#
# class Apple(Spam):
#     a = 20 # Overrides the value of class variable "a" in parent class
#     def google(self):
#         print('google')
#
# c1 =Spam()
# c1.apple()
# c2 = Apple()
# c2.google()
# c1.apple()
# print(c2.a)
# print(c1.a)b


# class BankAccount:
#     interest_rate = 4.0
#     def __init__(self, fname, lname, amount):
#         self.fname = fname
#         self.lname = lname
#         self.balance = float(amount)
#         self._transactions = []
#         self._transactions.append(f"Initial Deposit*** {self.balance}")
#
#     def deposit(self, amount):
#         self.balance += float(amount)
#         self._transactions.append(f'Deposited Amount: {amount}')
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             self._transactions.append(f'Withdrawn Amount: {amount}')
#         else:
#             raise InsufficientBalance()
#
#     def statement(self):
#         for line in self._transactions:
#             print(line)
#             print(f"Total Account Balance: {self.balance}")
#
#     def roi(self):
#         self.balance = self.balance + self.balance * (self.interest_rate / 100)
#
# class SavingsAccount(BankAccount):
#     interest_rate = 4.0
#     def withdraw(self, amount):
#         if amount > 10000:
#             raise MaxWithdrawLimtExceeded('Can not withdrawn more than 10000 per day')
#             super().withdraw(amount)
#
# c1 =BankAccount("shobha",'p',1000)
# print(c1.__dict__)
# print(c1.deposit(200000))
# print(c1.__dict__)
# c1.withdraw(200000)
# print(c1.__dict__)
# c2=SavingsAccount("shobha",'p',1000)
# c2.withdraw(1000)
# print(c2.__dict__)



# class Log:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("You called {self.func.__name__}")
#         return self.func(*args, **kwargs)
#
# @Log
# def add(a,b):
#     return a+b
# print(1,2)
#
# import time
# from time import sleep
# class Time:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         start = time.time()
#         result = self.func(*args, **kwargs)
#         end = time.time()
#         print(f'Execution Time: {end-start}')
#         return result
#
# def add(a,b):
#     sleep (2)
#     return a+b
# print(add(1,2))



# class LastChar:
#     def __call__(self, item):
#         return item[-1]
#
# items = ['bv', 'aw', 'dt', 'cu']
# last = LastChar()
# s = sorted(items, key=last)
# print(list(s))


# class Temperature:
#     def __call__(self, item):
#         return item[-1]
#
# temperatures = [('Bangalore', 25), ('Delhi', 45), ('Chennai', 37), ('Mumbai',55)]
# temperature =Temperature()
# l = sorted(temperatures, key=temperature)
# print(list(l))
#
# 6l = [('Bangalore', 25), ('Delhi', 52), ('Chennai', 37), ('Mumbai',55)]
# li = sorted(l,key=lambda item:item[-1])

# print(li)

li = [1,2,3,4,6,7]
def number(n):
    global li
    for index, value in enumerate(li):
        if n==value:
            return (index)
        else:
            li.append(n)
            li.sort()
        return (li.index(n))
print(number(5))

