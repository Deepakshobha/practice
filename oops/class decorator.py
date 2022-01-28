# def logging(some_class):
#     for key,value in some_class.__dict__.items():
#         if callable(value):
#             setattr(some_class,key,log(value)) #__init__ = log(__init__) add=log(add)
#         return some_class
# def log(func):
#     def wrapper(*args,**kwargs):
#         print(f"calling {func.__name__}")
#         result = func(*args,**kwargs)
#         return result
#     return wrapper
#
# @logging #calculator logging(calculator)
# class calculator:
#     name ='shobha'
#     def __init__(self,x,y):
#         self.a = x
#         self.b = y
#
#     def add(self):
#         return self.a+self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
# print(calculator.__dict__)
# print(calculator.__init__)

def attach(cls):
    cls.name = 'shobha'
    return cls

@attach
class demo:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b


d = demo(1,2)
f = attach('s')
print(dir(f))