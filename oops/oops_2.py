# class employee:
#     def __init__(self,fname,lname,pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#
#     def email(self):
#          return f'{self.fname},{self.lname}@company.com'
#
# e1=employee('steve','jobs',1000)
# print(e1.__dict__)
# print(e1.email())
# class calculator:
#     def __init__(self,x,y):
#         self.a = x
#         self.b = y
#
#     def add(self):
#         return self.a+self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
# c1 = calculator(1,2)
# c2 = calculator(10,20)
# c3 = calculator(13,25)
#
# print(c1.__dict__)
# print(c1.add())
# print(c1.sub())
# print(c1.mul())

#
# class points:
#     def __init__(self,x,y):
#         self.a = x
#         self.b = y
#
#     def move(self,dx,dy):
#         self.a += dx
#         self.b += dy
#
# c1 = points(1,2)
# c2 = points(10,20)
#
# print(c1.__dict__)
# c1.move(15,18)
# print(c1.a, c1.b)

class player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self,dx,dy):
        self.x += dx
        self.y += dy
        self.health = 100

    def attac(self,pts):
        self.health -= pts


p1 = player(4,5)
print(p1.__dict__)
p1.move(10,14)
print(p1.x,p1.y)
print(p1.__dict__)
p1.attac(25)
print(p1.x,p1.y)
print(p1.__dict__)
# print(p1.__class__.__dict__)
# print(player.__dict__)