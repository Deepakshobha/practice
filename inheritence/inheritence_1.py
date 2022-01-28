# class parent:
#     def __init__(self,value):
#         self.value = value
#
#     def google(self):
#         print(f"executing parent google {self.value}")
#
#
#     def apple(self):
#         print("executing parent apple")
#         self.google()
#
# # class child1(parent):   # adding parent class function to child1 parent
# #     def demo(self):
# #         print('Executing demo')
# #
# # #child override parent class method
# class child2(parent):
#     def hello_world(self):
#         print('hello world')
#     def google(self):
#         print(f'executing child2 google{self.value}')
#
# #child adding extra functionality re using the original functionality of the parent class
# class child3(parent):
#     def google(self):
#         print("executing child 3 google")
#         super().google()
#
# #child class having an extra attibutes
# class child4(parent):
#     def __init__(self,value,name): #(self,value,name) value from parent class attibute
#         self.name = name
#         super().__init__(value) # calling parent class attibute
#
# class facebook:
#     def spam(self):
#         print('executing facebook spam')
#
# #child inheriting from multiple parents
# class child5(parent,facebook):
#     pass


# # p1 = parent(10)
# # c = child1(15)
# d = child2(20)
# # # e = child3(40)
# f = child4(10,'shobha')
# print(f.__dict__)
# g = child5(55)
#
# # print(p1.__dict__)
# # p1.google()
# # p1.apple()
# # print(c.__dict__)
# # c.google()
# # c.apple()
# # c.demo()
# # print(d.__dict__)
# # d.apple()
# # d.hello_world()
# # d.google()
# # # d.spam()  # attribute error child2 not there in class child2
# # print(child2.__mro__) #method resulation order
# # print(e.__dict__)
# # e.apple()
# # e.google()
# # print(child3.__mro__) #method resulation order first checks attributes in child3 then parent the object class
#
# g.spam()
# g.apple()
# g.google()