#Variable overriding
# class A:
#     a = 10
# class B(A):
#     b = 20
#     a = 45
# obj = B()
# print(obj.a)

#override the constructor in dictionary
# class A:
#     def __init__(self):
#         print("inside A class")
# class B(A):
#
#     def __init__(self):
#         print("inside B class")
#
# # print(A.__dict__)
# obj = B()
# print(obj)
#

#chaining a constructor
# class A:
#     a = 20
#     def __init__(self):
#         print("inside A class")
# class B(A):
#     b = 50
#     def __init__(self):
#         A.__init__(self)
#         print("inside B class")

# print(A.__dict__)
# obj = B()
# print(obj.b)

#constructor
# class A:
#     a = 20
#     def __init__(self):
#         print("inside A class")
# class B(A):
#     b = 50
#     def __init__(self):
#         super().__init__()
#         print("inside B class")
#
# # print(A.__dict__)
# obj = B()
# print(obj.b)

#constructor with an argument
class A:
    a = 20
    def __init__(self,b):
        self.b = b
        print("inside A class",b)
class B(A):
    c = 50
    def __init__(self):
        super().__init__(25)
        print("inside B class")


obj = B()
# print(obj.b)


l1 = [1,2,3]
l2 = [4,5,6]
l3 = (*l1,*l2)
print(l3)
l3=list(l3)
print(l3.sort())


#constructor with method
class A:
    a = 10
    def __init__(self,b):
        self.b = b
        print("inside A class",b)
    def des(self):
        print(self.a,self.b)
class B(A):
    x = 45
    def __init__(self):
        super().__init__(25)
        print("inside B class")
    def des(self):
        super().des()
        print(self.x)


obj = B()
# print(obj.des())


#multi level inheritance
# class A:
#     a = 10
# class B(A):
#     b = 20
# class C(B):
#     d = 100
# print(C.a,C.b,C.d)

#multi level constructor
# class A:
#     a = 20
#     def __init__(self,b):
#         self.b = b
#         print("inside A class",b)
# class B(A):
#     b = 50
#     def __init__(self,c):
#         super().__init__(30)
#         print("inside B class",c)
# class C(B):
#     c = 68
#     def __init__(self):
#         super().__init__(50)
#         print("inside c class")
#
# obj = C()
# print(C.__mro__)


#relation ships
# class Grand_Father:
#     def __init__(self,name):
#         self.gname=name
# class father(Grand_Father):
#     def __init__(self,fname,gname):
#         self.fname =fname
#         super().__init__(gname)
# class Child(father):
#     def __init__(self,cname,fname,gname):
#         self.cname =cname
#         super().__init__(fname,gname)
#     def display(self):
#         print("grand father name is",self.gname)
#         print("father name is", self.fname)
#         print("child", self.cname)
# obj = Child("XYZ","xyz","123")
# print(obj.display())
#


#multiple inheritance
# class A:
#     x = 10
#     print(x)
# class B:
#      y = 20
#      print(y)
# class C(B,A):
#     print(50)
# obj = C()
# obj()

# class A:
#     def __init__(self):
#         print("in A")
# class B:
#     def __init__(self):
#         print("in B")
# class C(A,B):
#     print(50)
# obj = C()


#hybrid inheritance
class Vehicle:
    def __init__(self,company):
        self.company = company
    def disp(self):
        print("company",self.company)
class bike(Vehicle):
    def __init__(self,company,cost,model):
        super().__init__(company)
        self.cost = cost
        self.model = model
    def disp(self):
        print("cost",self.cost)
        print("cost", self.model)
class bike(Vehicle):
    def __init__(self,company,cost,model):
        super().__init__(company)
        self.cost = cost
        self.model = model
    def disp(self):
        print("cost",self.cost)
        print("cost", self.model)


