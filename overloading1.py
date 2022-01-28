
#constructor overloding
class point:
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

p1 =point(1,2,3,4)
p2 =point(1,2,4)
p3 =point(1,2,4,5)
p4 =point()
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)
print(p4.__dict__)

def add(a,b):
    return a+b

print(add(1,3))

print(dir(add))
print(dir(p1)) # class do not have __call so its not collable


# class greeting:
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self):             # making class collable
#         return f"hello {self.name}"
#
# g = greeting('shobha')
# print(g())


# class greeting:
#     def __call__(self,name):
#         return f"hello {name}"
#
# f = greeting()
# print(f('shobha'))

#
# class squares:
#     def __call__(self,numbers):
#         return [number ** 2 for number in numbers]


# count how many number of function called