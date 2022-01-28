
# position only
# def add_(a,b,/):
#     c = a+b
#     return c
# res = add_(1,2)
# print(res)

# keyword only
# def add_(*,a,b):
#     c = a+b
#     return c
# res = add_(b=2,a=1)
# print(res)

# position and keyword
# def add_(a,/,*,b):
#     c = a+b
#     return c
# res = add_(1,b=2)
# print(res)

# even numbers
# def list_(end,start=0):
#     l=[]
#     for i in range(start,end):
#         if i % 2 == 0:
#             l.append(i)
#     return l
#
# print(list_(21,5))

# prime number
# def list_(end,start=2):
#     l=[]
#     for n in range(start,end+1):
#         if n > 1:
#             for i in range(2,n):
#                 if n % i == 0:
#                     break
#             else:
#                 l.append(n)
#     return l
#
# print(list_(start=1, end = 50))

# fibonacii series
# a = 0
# b = 1
# i = 0
# while i < 10:
#     print(a)
#     c = a+b
#     a = b
#     b = c
#     i += 1

# def fib(n):
#     a = 0
#     b = 1
#     i = 0
#     while i < n:
#         # print(a)
#         c = a+b
#         a = b
#         b = c
#         i += 1
#     return a
#
# print(fib(10))


# def fib(n):
#     a = 0
#     b = 1
#     while a < n:
#         print(a)
#         c = a+b
#         a = b
#         b = c

# (fib(10))

# integer and float sum
#
# def add_(*args):
#     sum = 0
#     for i in args:
#         if isinstance(i,(int,float)):
#             sum += i
#     print(sum)
# add_(1,1.2,3+2j)

#
# number of positional arguments
# def add_(*args):
#     count = 0
#     for i in args:
#         count += 1
#     return count
# print(add_(1,1.2,3+2j))




# def count_(*args,**kwargs):
#     return args, kwargs
#
# print(count_(1,2,a=1,b=2))

#
# li = [1,2,3]
# def count_(*args):
#     if len(args) > 5:
#         return "greater"
#     else:
#         return "not a greater"

#print(count_(*li))

#
# print "hai everyone" if input not present else print input

# def user(*args):
#     if args:
#         print(args)
#     else:
#         print('hai')
# user()


# def user(msg = "hai every" ):
#     print(msg)
#
# user(1)

# def prime(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return 'not a prime'
#         return 'prime'
#
# print(prime(8))



# def prime(num):
#     for n in range(num):
#         if n > 1:
#             for i in range(2,n):
#                 if n % i == 0:
#                     break
#             else:
#                 print(n)
# (prime(11))


# li = [1,2,3]
# def count_(*args):
#     return args[-1]
#
# print(count_(*li))


# s = "shobha"
# n = 4
# def element(*args):
#     print(args[-n:])
#
# element(*s)


# def square(num):
#     for i in range(num):
#         if i*i == num:
#             return "True"
#     return "False"
#
# print(square(9))

# 0 - RCN
# 1 - TAX

# def func(string,n):
#     if n == 0:
#         return string[1::2]
#     elif n == 1:
#         return string[::2]
#     else:
#         return 'value invalid'
# print(func("TRACXN",1))

# l = []
# def fib(n):
#     a = 0
#     b = 1
#     while a <= n:
#         l.append(a)
#         c = a+b
#         a = b
#         b = c
#     print(l)
#     if n in l:
#         print('fibonacii')
#     else:
#         print('not fibonacii')
#
# (fib(40))


# l = []
# def fib(n):
#     a = 0
#     b = 1
#     while a <= n:
#         if a == n:
#             return 'fibonacii'
#         c = a+b
#         a = b
#         b = c
#
#     return 'not fibonacii'
#
# print(fib(3))
