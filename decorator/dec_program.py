
# logs message before executin function
# def log(func):
#     def wrapper(*args, **kwargs):
#         print('in decorator')
#         func(*args, **kwargs)
#     return wrapper
# @log
# def display():
#     print('in display')
# display()

# delay
import time
# def delay(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(2)
#         return func(*args, **kwargs)
#     return wrapper
# @delay
# def display():
#     return ('in display')
# print(display())

# string reverse
# def reverse(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)[::-1]
#         return res
#     return wrapper
# @reverse
# def spam(string):
#     return string
#
# print(spam('hai'))

# function with 3 times
# def reverse(func):
#     def wrapper(*args, **kwargs):
#         (func(*args, **kwargs))
#         (func(*args, **kwargs))
#         (func(*args, **kwargs))
#
#     return wrapper
# @reverse
# def spam(string):
#     print(string[::-1])
#
# (spam('hai'))

# function with n times
# def outer(n):
#     def repeat_(func):
#         def wrapper (*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return repeat_
# @outer(3)
# def add(a,b):
#     print(a+b)
#
# add(1,2)

# n delay
# import time
# def outer(n):
#     def repeat_(func):
#         def wrapper (*args, **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)
#         return wrapper
#     return repeat_
# @outer(3)
# def add(a,b):
#     print(a+b)
#
# add(1,2)
#
# @outer(2)
# def sub(a,b):
#     print(a-b)
#
# sub(1,2)

# calculate the time of execution
import time
def outer(n):
    time.sleep(n)
    def repeat_(func):
        def wrapper (*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print(f"time of execution is :{end-start}")
        return wrapper
    return repeat_
@outer(2)
def add(a,b):
    print(a+b)

add(1,2)


# count no of arguments pass to a function
# def count_(func):
#     def wrapper(*args,**kwargs):
#         func(*args, **kwargs)
#         print("count of input",len(args)+len(kwargs))
#     return wrapper
#
#
# @count_
# def spam(*args,**kwargs):
#     return (args,kwargs)
#
# spam([1,2,3],{'a':2},c={1,2},d=4)


# def count_(func):
#     def wrapper(*args,**kwargs):
#         print(f"you called {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @count_
# def add(a,b):
#     return a+b
#
# print(add(1,2))
#
# @count_
# def sub(a,b):
#     return a-b
#
# print(sub(1,2))


# def count_(func):
#     def wrapper(*args,**kwargs):
#         print(f"you called {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @count_
# def add(a,b):
#     return a+b
#
# print(add(1,2))
#
# @count_
# def sub(a,b):
#     return a-b
#
# print(sub(1,2))

#
# type string reversed
# def count_(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result,str):
#             return result[::-1]
#         return result
#     return wrapper
#
# @count_
# def add(a,b):
#     return a+b
#
# print(add(1,2))
#
# @count_
# def sub(a,b):
#     return a-b
#
# print(sub(1,2))
#
# @count_
# def greet():
#     return 'hello world'
#
# print(greet())


# positive
def positive_(func):
    def wrapper(*args,**kwargs):
        result = func(*args, **kwargs)
        if isinstance(result,(int,float)):
            return abs(result)
        return result
    return wrapper

@positive_
def sub(a,b):
    return a-b


@positive_
def sub(a,b):
    return a-b


@positive_
def greet():
    return 'hello world'


# execution time
# from time import time,sleep
# def positive_(func):
#     def wrapper(*args,**kwargs):
#         start = time()
#         func(*args, **kwargs)
#         end = time()
#         print(f"the execution time of {func.__name__} is {end-start}")
#     return wrapper
#
# @positive_
# def add(a,b):
#     return a+b
# (add(1,2))
#
# @positive_
# def sub(a,b):
#     sleep(6)
#     return a-b
# (sub(1,2))
#
# @positive_
# def greet():
#     sleep(3)
#     return 'hello world'
# greet()



# 1 counting function calls
# from collections import defaultdict
# dd = defaultdict(int)
# def count_(func):
#     def wrapper(*args,**kwargs):
#         dd[func.__name__] += 1
#         func(*args, **kwargs)
#         return dd
#     return wrapper
#
# @count_
# def add(a,b):
#     return a+b
# print(add(1,2))
#
# @count_
# def add(a,b):
#     return a+b
# print(add(1,2))
#
# @count_
# def sub(a,b):
#     return a+b
# print(sub(1,2))
#
# @count_
# def greet():
#     return 'hello world'
# print(greet())


# 2 counting function calls
# def count_(func):
#     func.count = 0
#     def wrapper(*args,**kwargs):
#         func.count += 1
#         result = func(*args, **kwargs)
#         print(f"function {func.__name__} was invoked {func.count} times")
#         return result
#     return wrapper
#
# @count_
# def add(a,b):
#     return a+b
# print(add(1,2))
#
# @count_
# def add(a,b):
#     return a+b
# print(add(1,2))
#
# @count_
# def sub(a,b):
#     return a+b
# print(sub(1,2))
#
# @count_
# def greet():
#     return 'hello world'
# print(greet())


# maximum 3
# def maximum_(func):
#     func.count = 0
#     def wrapper(*args,**kwargs):
#         func.count += 1
#         if func.count > 3:
#             raise ValueError("maximum limit excedded")
#         func(*args, **kwargs)
#         print(func.count)
#
#     return wrapper
#
# @maximum_
# def add(a,b):
#     return a+b
from time import sleep
# repeat functions
# def maximum_(func):
#     def wrapper(*args,**kwargs):
#         for i in range(2):
#             return func(*args, **kwargs)
#             sleep(3)
#     return wrapper
#
# @maximum_
# def add(a,b):
#     return a+b
#
# print(add(1,2))
# print(add(1,2))


# cache counter
from time import sleep


# def cache(func):
#     func.d = {}
#
#     def wrapper(*args, **kwargs):
#         if args in func.d:
#             print('getting result from cache')
#             print(func.d)
#         print('execution for the first time')
#         result = func(*args, **kwargs)
#         func.d[args] = result
#         print(func.d)
#
#     return wrapper
#
#
# @cache
# def add(a, b):
#     return a + b
#
#
# add(1, 2)
# add(1, 2)
# add(1, 2)

#list of numbers is 10 add prefix +91-, 12 numbers with 91 add +- other number return
# numbers= [123456789,3456789788,912345678990, 12343435369]
# def add_prefix(number):
#     str_number = str(number)
#     if len(str_number) == 10:
#         str_number = "+91-" + str_number
#         return str_number
#     elif len(str_number) == 12 and str_number.startswith("91"):
#         str_number = '+' + str_number[:2] + '-' +str_number[2:]
#         return str_number
#     else:
#         return str_number
#
# def prefix(func):
#     def wrapper(*args,**kwargs):
#         numbers = args
#         prifix_numbers = [add_prefix(number) for number in numbers]
#         print(func(prifix_numbers))
#     return wrapper
#
# @prefix
# def print_numbers(numbers):
#     for number in numbers:
#         print(number)
#
#
# print_numbers(*numbers)

#type validator for function argument
# def validate(*types):
#     def _validated(func):
#         def wrapper(*args,**kwargs):
#             for _arg,_type in zip(args,types):
#                 if not isinstance(_arg,_type):
#                     raise TypeError(f"invalid type passes for {_arg}")
#             return func(*args,**kwargs)
#         return wrapper
#     return _validated
#
# @validate(int,int)
# def add(a,b):
#     print("executing add")
#     return a+b
#
# print(add(1,5))
# @validate(int,int)
# def sub(a,b):
#     return a-b
# print(sub(1,2))
#
# @validate(str,int,float)
# def greet(name,age,pay):
#     return (f"hello{name} you are {age} years you {pay}")
# print(greet("shobha",30,35000.00))


#separate function for type checking
def type_check(actual_values, expected_values):
    for _type, _value in zip(expected_values,actual_values):
        if not isinstance(_value,_type):
            raise TypeError
        # print(f"{_type}and {_value} are matching ")
# type_check((10,20.0,30),(int,float,int))


# alternate solution using keyword argument
# def validate(**types):
#     def _validated(func):
#         def wrapper(*args,**kwargs):
#             _actual_values = list(args)
#             _expected_values = list(types.values())
#             type_check(_actual_values,_expected_values)
#             return func(*args,**kwargs)
#         return wrapper
#     return _validated
#
# @validate(a=int,b=int)
# def add(a,b):
#     print("executing add")
#     return a+b
#
# print(add(1,5))
# @validate(a=int,b=int)
# def sub(a,b):
#     return a-b
# print(sub(1,2))
#
# @validate(name=str,age=int,pay=float)
# def greet(name,age,pay):
#     return (f"hello{name} you are {age} years you {pay}")
# print(greet("shobha",30,35000.00))


#as long as value error re execute the program
# def retry(func):
#     def wrapper(*args,**kwargs):
#         while True:
#             try:
#                 return func(*args, **kwargs)
#             except ValueError:
#                 print("retrying")
#     return wrapper
# import random
# @retry
# def dice():
#     number = random.randint(1,10)
#     if number != 8:
#         raise ValueError
#     else:
#         return number
# print(dice())

#execute a function for 3 times
def retry(func):
    def wrapper(*args,**kwargs):
        max_tries = 3
        while max_tries > 0:
            try:
                max_tries -= 1
                return func(*args, **kwargs)
            except ValueError:
                print(f"invalid creds,atempts left{max_tries}")
                if max_tries == 0:
                    print("account is locked")
    return wrapper

@retry
def login():
    username = input('enter user name:')
    password = input('enter the password')
    if username == 'admin' and password == 'Password123':
        return "login is succesfull"
    else:
        raise ValueError('invalid credential')
print(login())