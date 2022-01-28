# class Parent:
#     name = "Ram"
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# p = Parent(1, 2)
# c = Child1(12, 45)
# print(c.name)
# print(c.__dict__)

class Parent1:
    a = 10
    def display(self):
        print("in parent1 display")

class Parent2:
    b = 25
    def abc(self):
        print("in parent2 display")

class Child(Parent2, Parent1):
    a = 80

    def display(self):
        print("in Child display")

        super().abc()
        super().display()
        # Parent2.display(self)

c = Child()
c.display()
print(Child.__mro__)
#
#
# class Sample:
#     """ This class is built for displaying some message"""
#
#     def __init__(self):
#         pass
#
#     def display(self):
#         pass
#

# printing documentation string
# print(Sample.__doc__)









































