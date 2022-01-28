#compiler polymorphism
from functools import singledispatch

@singledispatch
def add(a,b):
    print("base method")
    return a + b

@add.register(int)
def _(a,b):
    print("calling int")
    return a+b

@add.register(float)
def _(a,b):
    print("calling float")
    return a+b

@add.register(list)
def _(a,b):
    print("calling list")
    return sum(a) + b

add([1,2],2)
add(1,2)
add(1.2,2)
