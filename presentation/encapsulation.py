#single underscore
# class Base:
#     def __init__(self):
#         self._a = 2 #protected member
#
#
# obj1 = Base()
# print(obj1._a)
# print(obj1._a) # we can access and modify but we should't  as per the convention

#double underscore
# class Base:
#     __a = 20
#     print(__a)
#     def __init__(self):
#         self.b = "hello"
#         print(self.b)
# obj = Base()
# obj.__a


# Access private member
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary
# #
# # creating object of a class
# emp = Employee('Jessa', 10000)
#
# print('Name:', emp.name)
# # direct access to private member using name mangling
# print('Salary:', emp._Employee__salary)
# print(emp.salary)


#getter and setter in python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private member

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age

stud = Student('Jessa', 14)

print(stud.name)
# print(stud.age)
# retrieving age using getter
print('Name:', stud.name, stud.get_age())

# changing age using setter
stud.set_age(16)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())


# Example: Information Hiding and conditional logic for setting an object attributes
class Student:
    def __init__(self, name, roll_no, age):
        # private member
        self.name = name
        # private members to restrict access
        # avoid direct data modification
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__roll_no)

    # getter methods
    def get_roll_no(self):
        return self.__roll_no

    # setter method to modify data member
    # condition to allow data modification with rules
    def set_roll_no(self, number):
        if number > 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.__roll_no = number

jessa = Student('Jessa', 10, 15)

# before Modify
jessa.show()
# changing roll number using setter
jessa.set_roll_no(120)


jessa.set_roll_no(25)
jessa.show()