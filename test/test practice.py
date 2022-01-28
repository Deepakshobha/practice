# # 1 sort list from a to z
#
# l =["hello",'ball','zebra','yak','apple']
# res=(sorted(l))
# # print(res)
#
# # 2 this world not enough sort based on length
# s="this world not enough"
# r = s.split()
# res=sorted(r,key=len)
# # print(res)
#
# # 3 sort based on last letter
# l =["hello",'ball','zebra','yak','apple']
# # print(sorted(l,key = lambda item:item[-1]))
#
# # 4 based on length key
# # d={'flipkart':10,'walmart':13,'gmail':23}
# # print(sorted(d,key=len))
# #
# # 5 sort based on value
# # d={'flipkart':10,'walmart':13,'gmail':23}
# # print(sorted(d.items(),key=lambda item:item[1]))
# #
# # 6 anagram
# # def func(*args):
# #     if sorted(args[0]) == sorted(args[1]):
# #         return ("anangram")
# #     return 'not a anangram'
# # print(func('tea','eat'))
#
#
# a = '(({[]}))'
# b = a[::-1]
# i = 0
# while i != len(a) - 1:
#     if ord(a[i]) == ord(a[i]) + 1 or ord(a[i]) + 2:
#         print(True)
#     else:
#         print(False)
# i += 1
#
# # 7 shares > 40
# from collections import defaultdict
# dd = defaultdict(int)
# d={'acne':45.23,'aapl':612.78,'ibm':205.55,'hpq':37.20,'fb':10.75}
# res=dict(sorted(d.items(),key=lambda item:item[1]))
# for key,value in res.items():
#     if res[key] > 40:
#         dd[key] = value
# print(dd)


# p=[{'name':'1','shares':5,'price':2},
#    {'name':'1','shares':5,'price':2},
#    {'name':'1','shares':8,'price':2},
#    {'name':'1','shares':3,'price':2},
#    {'name':'1','shares':4,'price':2}]
# print(sorted(p,key=lambda item:item['shares']))

# 9 most reapeated character
from collections import Counter
# s = "hiiiii iiii hello hi"
# res =Counter(s)
# print(res.most_common(1))


#
# a = "123$"
# print("a".isidentifier())
# print(help("keywords"))
# a=25
# b=15
# print(divmod(a, b))
# print("hai \task python\n")
# a = "hello"
# print(a[:-3])
# s = "the value of pi %0.4f" % (3.14592)
# print(s)
# a = "hello world"
# print(a.rindex('l',1,6))
# print(a)
# b = "hello world"
# print(b.replace("hello","universe"))
# print(b)
# a = " "
# print(a.join(['helloworld','universe']))

# a = "****$$$'hai'#$*="
# print(a.strip('*$='))
# print(a.rstrip('='))
# b = [1, 2,3]
# del b[0]
# print(b)

# a = [1, 2, 3]
# b = a.copy()
# a.append(4)
# print(a)
# print(b)
# print(id(a))
# print(id(a))
#
# from copy import deepcopy
# a = [1, 2, 4, [10, 20]]
# b = deepcopy(a)
# a[3].append(30)
# print(a)
# print(b)
# print(id(a))
# print(id(a))

# s = [1,2,3,4,5,6,(3,4)]
# b = str(s)
# print(b)
# print(''.join(b))
# a={1,2,3,4}
# x={1,4}
# print(x.issuperset(a))
# # print(a.update([6,7,8]))
# # print(a)
#
# # d={}
# # d['mysore'] =10
# # print(d)
# # d.update({'coachin':28})
# # print(d)
# # d.update(('coachin'=26))
# # print(d)
#
# # d = {'a':1,'b':2,'c':3}
# # print(d.pop())
#
# # d1 = {'name':'steve','age':12}
# # d2 = {'name':'clark','company':'del'}
# # d3 = d1|d2
# # print(d3)
# #
# #
# # a = 'shobha123'
# # count = 0
# # for i in a:
# #     if i.isdigit():
# #         count += 1
# # print(count)
#
#
# l = [1,2,3,4,5]
# for n in l:
#     if n>1:
#         for i in range(2,n):
#             if n%i == 0:
#                 break
#         else:
#             print(n)



# longest not repeated word
# s = "this is a programming language and programming is fun"
# r = s.split()
# res = Counter(r)
# for key,value in res.items():
#     if res[key] == 1:
#         dd[key] = value
# res=(sorted(dd.keys(),key=lambda item:len(item)))
# print(res[-1])

# """ WAP to check if the given input number is even"""
# a = int(input('enter the value'))
# if a%2 == 0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")


# b = '(({[]})}'
# a = b[::-1]
# i = 0
# while i < len(b)//2:
#     if ord(a[i]) == ord(b[i]) + 1 or ord(a[i]) == ord(b[i]) + 2:
#         print(True)
#     else:
#         print(False)
#     i += 1


d = {'1':True,'2':False,'3':True,'4':False}
l = []
for i in d:
    if d[i] == True:
        l.append(i)
        d[i]='pass'
print(l)
print(d)

