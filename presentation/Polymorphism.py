#method overloading
def add(a,b):
    print(a+b)
add(1,2)

def add(a,b,c):
    print(a+b+c)
add(1,2)

# def add(a=0,b=0,c=0):
#     print(a+b+c)
# add(1,2)

# operator overloading
# add 2 numbers
# print(100 + 200)
#
# # concatenate two strings
# print('Jess' + 'Roy')
#
# # merger two list
# print([10, 20, 30] + ['jessa', 'emma', 'kelly'])
#
#
# # overloading with custom objects
# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
# # creating two objects
# b1 = Book(400)
# b2 = Book(300)

# add two objects
# print(b1 + b2)


# magic method __add__
class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading + operator with magic method
    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(400)
b2 = Book(300)
print("Total number of pages: ", b1 + b2)



# Overrride Built-in Functions
class Shopping:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        print('Redefine length')
        count = len(self.basket)
        # count total items in a different way
        # pair of shoes and shir+pant
        return count * 2

shopping = Shopping(['Shoes', 'dress'], 'Jessa')
print(len(shopping))


# Polymorphism In Class methods
# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")
#
#     def max_speed(self):
#         print("Max speed 350")
#
# class BMW:
#     def fuel_type(self):
#         print("Diesel")
#
#     def max_speed(self):
#         print("Max speed is 240")
#
# ferrari = Ferrari()
# bmw = BMW()
#
# # iterate objects of same type
# for car in (ferrari, bmw):
#     # call methods without checking class of object
#     car.fuel_type()
#     car.max_speed()

#function object
# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")
#
#     def max_speed(self):
#         print("Max speed 350")
#
# class BMW:
#     def fuel_type(self):
#         print("Diesel")
#
#     def max_speed(self):
#         print("Max speed is 240")
#
# # normal function
# def car_details(obj):
#     obj.fuel_type()
#     obj.max_speed()
#
# ferrari = Ferrari()
# bmw = BMW()
#
# car_details(ferrari)
# car_details(bmw)


#method overloading
# def addition(a, b):
#     c = a + b
#     print(c)
#
#
# def addition(a, b, c):
#     d = a + b + c
#     print(d)
#
# def addition(a=0, b=0, c=0,d=0):
#     d = a + b + c +d
#     print(d)
# # the below line shows an error
# # addition(4, 5)
#
# # This line will call the second product method
# addition(3, 7, 5,5)



# class Shape:
#     # function with two default parameters
#     def area(self, a, b=0):
#         if b > 0:
#             print('Area of Rectangle is:', a * b)
#         else:
#             print('Area of Square is:', a ** 2)
#
# square = Shape()
# square.area(5)
#
# rectangle = Shape()
# rectangle.area(5, 3)
#


#operator overloading
# # add 2 numbers
# print(100 + 200)
#
# # concatenate two strings
# print('Jess' + 'Roy')
#
# # merger two list
# print([10, 20, 30] + ['jessa', 'emma', 'kelly'])


#overloading with custom objects
# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#
# # creating two objects
# b1 = Book(400)
# b2 = Book(300)
#
# # add two objects
# print(b1 + b2)


#magic method __add__
class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading + operator with magic method
    def __add__(self, other):
        return self.pages + other.pages


b1 = Book(400)
b2 = Book(300)
print("Total number of pages: ", b1 + b2)


#magic method __mul__
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, timesheet):
        print('Worked for', timesheet.days, 'days')
        # calculate salary
        return self.salary * timesheet.days


class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days


emp = Employee("Jessa", 800)
timesheet = TimeSheet("Jessa", 50)
print("salary is: ", emp * timesheet)