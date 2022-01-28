""" Positional arguments """
def greet(name, age):
    print(f"{name} is {age} years old")


# greet("Ram", 50)
# greet(50, "Ram")

""" keyword arguments """
def greet(name, age):
    print(f"{name} is {age} years old")


# greet(name="Ram", age=20)
# greet(age=20, name="Ram")

""" combination of keyword and position"""
def add_(a, b, c, d):
    print(a, b, c, d)


# add_(1, 2, 3, 4)
# add_(a=1, b=2, c=3, d=4)
# add_(1, 2, c=3, d=4)
# add_(a=1, b=2, 3, 4)    # syntax error

""" positional only arguments """
def add_(a, b, c, d, /):
    print(a, b, c, d)


# add_(1, 2, 3, 4)
# add_(a=1, b=2, c=3, d=4)  # TypeError

def add_(a, b, /, c, d):
    print(a, b, c, d)

# add_(1, 2, 3, 4)
# add_(1, 2, c=3, d=4)
# add_(a=1, b=2, c=3, d=4) # TypeError

""" keyword only arguments """

def add_(*, a, b, c, d):
    print(a, b, c, d)

# add_(a=1, b=2, c=3, d=4)
# add_(1, 2, 3, 4)      # TypeError
# add_(1, 2, c=3, d=4)  # TypeError


# def add_(a, b, *, c, d):
#     print(a, b, c, d)

# add_(1, 2, c=3, d=4)
# add_(a=1, b=2, c=3, d=4)
# add_(1, 2, 3, 4)    # TypeError


# combination of * and /

# def add_(a, b, /, *, c, d):
#     print(a, b, c, d)


# add_(1, 2, c=3, d=4)
# add_(1, 2, 3, 4)  # TypeError

""" variable positional arguments """

def spam(*args):   # packing
    print(args)


# spam(1, 2, 3)

""" sum of the arguments """

def sum_(*args):
    print(args)
    # print(sum(args))
    total = 0

    for i in args:
        if isinstance(i, (int, float)):
            total += i
    return total

# print(sum_(1, 2))


""" no of positional arguments """

def function(*args):
    # count = 0
    # for _ in args:
    #     count += 1
    #
    # return count
    return len(args)

# print(function(1, 2, 3, 4, 5))

""" return all the integer values """

def int_data(*args):
    for item in args:
        if isinstance(item, int):
            print(item)

# int_data(1, 2.3, "hai", 19, 47, 1+0j)

""" return the reversed string """

def reverse_(*args):
    res = []
    for item in args:
        if isinstance(item, str):
            res.append(item[::-1])
    return res

# print(reverse_(1, 2, "hai", "bye"))


""" variable keyword arguments """

def keyword_args(**kwargs): # packing
    return len(kwargs)


# print(keyword_args(a=1, b=2, c=3, d=4))


""" no of positional and keyword"""
def count_(*args, **kwargs):
    return len(args), len(kwargs)


# print(count_(1, 2, 3, a=10, b=20, c=30))

# packing

def packing_args(*args, **kwargs):
    return args, kwargs


# print(packing_args(1, 2, 3, a=10, b=20))

# unpacking in print()
l = [1, 2, 3]
print(*l)   # 1 2 3
#
# d = dict(a=1, b=2, c=3)
# print(*d)   # a b c
# print(**d)  # TypeError


# unpacking in user defined function
l = [1, 2, 3, 4]

def unpacking_args(a, b, c, d):
    return a, b, c, d

# print(unpacking_args(*l))


""" no of arguments is greater than 5 or not """

def spam(*args):
    if len(args) > 5:
        return "number of args > 5"
    return "number of args < 5"

# print(spam(9, 2, 7, 6, 4, 3, 8))

""" print 'hai everyone' if the user input is not present"""

def display(msg="hai everyone"):
    print(msg)


# display("hello")
# display()



































































































