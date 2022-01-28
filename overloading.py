# def add(a,b):
#     return a+b
#
# def add(a,b,c):
#     return a+b+c
#
# def add(a,b,c,d):
#     return a+b+c+d
#
# print(add(1,2))
#
# class demo:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __init__(self,a,b,c,d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
# p1 =demo(1,2)
# print(p1.__dict__)
# # d = demo(1,2)
# # print(d)
# d = demo(1,2,3,4)
# print(d.__dict__)


class point:
    def __init__(self,*args):
        for i in args:
            self.args = args

p1 =point(1,2)
print(p1.__dict__)

