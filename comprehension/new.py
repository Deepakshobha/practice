# # li = ["python", 10, 3.2, 'selenium_','java']
# # for index, item in enumerate(li):
# #     print(index,item)
#
# # li = ["python", 10, 3.2, 'selenium_','java']
# # for i in range(len(li)):
# #     print(i,li[i])
#
# # li = ["python", 'selenium_','java']
# # for i in range(0,len(li),2):
# #     print(i)
#
# # d = {'user id':'shobhahdp','password':123456}
# # userid = input('enter user id:')
# # password = int(input('enter user id:'))
# # if d['user id'] == userid and d['pass word'] == password:
# #     print('login')
# # else:
# #     print('user id or password incorrect')
# #
# #
# # li =['python', "PHP",'java']
# # s = set()
# # for i in li:
# #     if i[0] in "pP":
# #         s.add(i)
# # print(s)
# #
# # li = [[1,2,3],[4,5,6],[7,8,9]]
# # outer = 0
# # l = []
# # for i in li:
# #     inner = 0
# #     for j in i:
# #         inner += j
# #     l.append(inner)
# # print(l)
# # for k in l:
# #     outer += k
# # print(outer)
# #
# # n = 100
# # for i in range(2,n):
# #     if i % 2 == 0:
# #         pass
# #     else:
# #         print(i, end =',')
#
# items =['apple',1.2,'google',12.6,26,'100']
# output = []
# for i in range(-2,len(items)-2,1):
#     output.append(items[i])
# print(output)

#
a = ['apple.com','ball.in','ball.in','cat.com','apple.net','apple.net']
c = []
g1 = []
for i in a:
    b = i.split('.')
    c.extend(b)
    d = (c[1::2])
print(d)



# from sys import getrecursionlimit
# print(getrecursionlimit())

# from sys import setrecursionlimit
# setrecursionlimit(2000)
# from sys import getrecursionlimit
# print(getrecursionlimit())



