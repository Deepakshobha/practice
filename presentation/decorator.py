# def outer(func):
#     print("hello")
#     def inner():
#         print("inside inner")
#         func()
#     return inner
# outer()
# res = outer()
# res()
# def add():
#     print('inside function')
#
# add = outer(add)
# add()
#
#
# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#         return func(a, b)
#     return inner
#
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
# divide(1,2)

#take string and reverse it
# def outer(func):
#     def inner(*args):
#         print(args[::-1])
#         print(func(*args))
#     return inner
# @outer
# def s(msg):
#     return msg
#
# (s("python"))

#execute function for 3 times
def outer(func):
    def inner(*args,**kwargs):
        for i in range(3):
            func(*args)
    return inner
@outer
def add(a,b):
    print(a+b)
# add(1,2)

#parameterised decorator 3 times
# def outer(n):
#     def inner(func):
#         def sinner(*args,**kwargs):
#             for i in range(n):
#                 func(*args)
#         return sinner
#     return inner
# @outer(3)
# def add(a,b):
#     print(a+b)
# add(1,2)

#chaining decorator
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)

# printer("Hello")


# def hello_dec(func):
#     def inner1():
#         print("hello before function")
#         func()
#         print("after execution")
#     return inner1
# def func_to():
#     print('this inside the function')
#
# func_to=hello_dec(func_to)
# func_to()

# def outer():
#     print("hello")
#     def inner():
#         print("inside inner")
#     return inner
# outer()

# def logger(func):
#     def inner(*args,**kwargs):
#         print('arguments are {},{}'.format(args,kwargs))
#         result= func(*args,**kwargs)
#         print(result)
#     return inner
# @logger
# def add_(x,y):
#     return x+y
#
# add_(1,2)



# def spam(func):
#     print("hello")
#     def wrapper():
#         print('in wrapper')
#         func()
#     return wrapper
# def add_():
#     print("outer")
# a = spam(add_)
# a()






def spam(x):
    def inner(*args):
        x(*args)
    return inner


def add(a, b):
    print(a + b)


add = spam(add)
add(1, 2)



def sub(x, y, z):
    print(x - y - z)

sub = spam(sub)
sub(1, 2, 3)





class demo:
    pass


print(demo())
print(dir(demo))



