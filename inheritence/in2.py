# Multi level inheritence
# class A:
#     def demo(selfself):
#         print('class a demo')
#
#
# class B(A):
#     def demo(selfself):
#         print('class b demo')
#         super().demo()
#
#
# class C(B):
#     def demo(self):
#         print('class c demo')
#         super().demo()

class parent:
    def demo(self):
        print('class parent demo')


class Demo(parent):
    def demo(self):
        print('class child1, demo')
        super().demo()


class spam(parent):
    def demo(self):
        print('class child2, demo') # first checks demo is there or not first executes demo
        super().demo()         #demo is not there access the parent attribute demo

class child(spam,Demo): # order of attributes matters first  spam then demo
    pass

c=child()
# c.demo()
# print(child.__mro__)

# c.demo()
print(child.__mro__)
c.spam()
