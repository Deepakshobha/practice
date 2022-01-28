# class Demo:
#     x = 10
#     y = 20
#
#     def __init__(self):
#
#     def display(self, name):
#         print("in display")
#         print(name)
#
#
# a = Demo("john")
# b = Demo()
# a.display("john")
# b.display("ram")
# Demo.display(a, "sita")
#
#
# #creating an class states/variables
# class demo1:
#     a =10
#     b = 20
#
# obj = demo1()
# #modification wrt class
# demo1.a=30
# print(demo1.a)
# #modification wrt obj
# obj.a=50
# print(obj.a)

# class A:
#     def __init__(self):
#         print("inside the constructor")
# A()

#constructor with argument
class B:
    a = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print("with in init of self",self)
obj = B(20,30)   # with in init of self <__main__.B object at 0x000001D2C4820E20>
print(obj.a)      # 10
print(obj.x)      #20
print(obj.y)      #30
print(obj.__dict__) #{'x': 20, 'y': 30}
print(B.a)    # 10
print(B.x) #type object 'B' has no attribute 'x'


# class Customer():
#     bankname='sbi'
#     ifsccode = "sbi000123"
#     manager = "shiva"
#     def __init__(self,name,age,email):
#         self.name=name
#         self.age=age
#         self.email=email
# obj=Customer("sho",25,"sh@")
# print(obj.bankname)
# print(obj.name,obj.bankname)


#object method
# class A:
#     a =10
#     def dis(self):
#         print("object method")
# obj=A()
# print(A.a)
# print(A.dis(obj))
# print(obj.dis()) # A.dis(obj) internally



# getmethod
# class A:
#     def __init__(self,a,b):
#         self.a =a
#         self.b = b
#     def getmethod(self):
#         print("self.a",self.a)
#         print("self.a",self.b)
#
# obj =A(10,20)
# print(A.getmethod(obj))
# print(obj.getmethod())



























