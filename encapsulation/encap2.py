# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def circumcircle(self):
#         return 2*3.14 * self.radius
#
# c1 = circle(5)
# print(c1.__dict__)
# print(c1.circumcircle())
# c1 = circle('2')
# print(c1.__dict__)
# c1.circumcircle()
# print(c1.__dict__)



# class circle:
#     def __init__(self,radius):
#         print('getting value from radius')
#         self.radius = radius #calls setter method
#     #_ attributes represents its for internal use
#     #getter method
#     @property
#     def radius(self):
#         return self._radius
#     #setter method
#     @radius.setter
#     def radius(self,value):
#         print(f"setting the radius value {value}")
#         if not isinstance(value,(float,int)):
#             raise TypeError("the radius should be number")
#         self._radius = value
#
#     def circumcircle(self):
#         return 2*3.14 * self.radius
#
# c1 = circle(3.1)
# print(c1.__dict__)
# print(c1.circumcircle())
# c1 = circle('2')
# print(c1.__dict__)
# c1.circumcircle()
# print(c1.__dict__)

# class person:
#     def __init__(self,fname,lname,age):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#     @property
#     def fname(self):
#         print("getting")
#         return self._fname
#
#     @fname.setter
#     def fname(self,value):
#         print('setting')
#         if not isinstance(value,str):
#             raise TypeError()
#         if len(value) > 5:
#             raise ValueError("fname should be less than 5 letter")
#         self._fname = value
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self,value):
#         if value<10 or value>60:
#             raise ValueError()
#         self._age = value
#
# p1 = person("abc",20,20)
# print(p1.__dict__)


class A:
    def __init__(self):
        self.__value = 0
        self._value = 10

    def demo(self):
        print(self._value)
        print(self.value)


d = A()
d._value = 10
print(d._value)
# print(d.__value)
d._A__value = 200
print(d._A__value)

#double underscorevattributes are called private attributes
#single underscorevattributes are called protected attributes
