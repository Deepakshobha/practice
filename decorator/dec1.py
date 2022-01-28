import time
from time import sleep
#log decorator
# def logging(msg = "hello world",debug=True):
#     def log(func):
#         def wrapper(*args,**kwargs):
#             if debug:
#                 print(msg, func.__name__)
#             return func(*args, **kwargs)
#         return wrapper
#     return log
#
# @logging(msg = "shobha",debug = False )
# def add(a,b):
#     return a,b

# print(add(1,2))

#delay decorator
# def _delay(_time_delay):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(_time_delay)
#             return func (*args, **kwargs)
#         return wrapper
#     return delay
# @_delay(2)
# def add(a,b):
#     return a+b
#
# print(add(1,2))

#reverse decorator
# def reverse(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args,**kwargs)
#         for i in result:
#             if isinstance(i,str):
#                 print(i[::-1])
#             else:
#                  print(i)
#     return wrapper
# @reverse
# def values(*args):
#     return args
#
# (values(1,2,3,'hai',4,'hello'))

# execution time
# def _delay(n):
#     time.sleep(2)
#     def asd(func):
#         def wrapper(*args):
#             start = time.time()
#             func(*args)
#             end = time.time()
#             print(f'execution time is {end-start}')
#         return wrapper
#     return asd
#
# @_delay(2)
# def add(a,b):
#     print(a+b)
# add(1,2)

#
# positive decorator
# def pos(func):
#     def wrapper(*args):
#         for i in args:
#             print(abs(i))
#         return func(*args)
#     return wrapper
#
# @pos
# def value(*args):
#     return args
#
# value(-1,2,4,-5)
#
#
#dictionary key as args output as value
# def cache(func):
#     _cache = {}
#     def wrapper(*args):
#         if args not in _cache:
#             result = func(*args)
#             _cache[args] = result
#         print('returning chache result')
#         print(_cache)
#     return wrapper
#
# @cache
# def add(a,b):
#     return a+b
#
# (add(1,2))
#
# @cache
# def sub(a,b):
#     return a-b
#
# (sub(1,2))


#repeat function n times
# def times(n):
#     def number(func):
#         def wrapper(*args):
#             for i in range(n):
#                 result = func(*args)
#                 print(result)
#         return wrapper
#     return number
# @times(3)
# def sub(a,b):
#     return a-b
#
# (sub(1,2))


#counting number of function callls
# from collections import defaultdict
#
# def number(func):
#     d = defaultdict(int)
#     def wrapper(*args):
#         d[func.__name__] += 1
#         func(*args)
#         return d
#     return wrapper
# @number
# def sub(a,b):
#     return a-b
#
# (sub(1,2))
# print(sub(1,2))
# print(sub(1,2))

#restrict the calls
# from collections import defaultdict
# dd =defaultdict(int)
# def number(n):
#     def max(func):
#         def wrapper(*args):
#             dd[func.__name__] += 1
#             if dd[func.__name__] > n:
#                 raise Exception("max limit execeeded")
#             result = func(*args)
#             print(result)
#         return wrapper
#     return max

# @number(2)
# def add(a,b):
#     return a+b
#
# add(1,2)
# add(1,2)

# @number(3)
# def sub(a,b):
#     return a-b
#
# sub(1,2)
# sub(1,2)
# sub(1,2)
# sub(1,2)

#phone numbers
numbers = ['1234567890','2255668899','9112345678','123456789']
def phnum(func):
    def wrapper(*args):
        for _ in args:
            if len(_) == 10:
                print('+91-' + _)
            elif len(_) == 12 and _.startswith('91'):
                print('+' + _[0:1] + '-' + _[2::])
            else:
                print(_)
        func(*args)
    return wrapper
@phnum
def ph(*args):
    for i in args:
        return i

(ph(*numbers))




