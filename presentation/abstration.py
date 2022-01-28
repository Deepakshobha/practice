from abc import ABC, abstractmethod
class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")
#
#
# # Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

#more methods
# class Polygon(ABC):
#
#     @abstractmethod
#     def noofsides(self):
#         pass
#     @abstractmethod
#     def display(self):
#         pass
#
# class Triangle(Polygon):
#
#     # overriding abstract method
#     def noofsides(self):
#         print("I have 3 sides")
#
# R = Triangle()
# R.noofsides() #error we need to declare all the methods in child class

import abc
# from abc import ABC, abstractmethod
#
#
# class R(ABC):
#
#     def rk(self):
#         print("Abstract Base Class")
#
#
# class K(R):
#     pass
#     # def rk(self):
#     #     super().rk()
#     #     print("subclass ")
#
#
# # Driver code
# r = K()
# r.rk()

