# add = lambda a,b: a+b
# print (add(1,2))
#
# even = lambda num : num % 2 == 0
# print(even(4))
#
# multi = lambda a,b : a * b
# print(multi(4,5))

# element = lambda num: num[-1]
# print(element([1,2,3]))

# pali = lambda s: s == s[::-1]
# print(pali("mom"))

# check = lambda num : f"{num} is even" if num % 2 == 0 else f"{num} is odd number"
# print(check(3))

# li =['hai','mom','dad']
# pali = lambda s: f"{s} is a palindrome" if s == s[::-1] else f"{s} is a not palindrome"
#
#
# res=(map(pali,li))
# print(list(res))

# li =[1,2,3,4,55,66,88,99]
# evenodd = lambda num: f"{num} is a even" if num % 2 == 0 else f"{num} is a odd"
#
#
# res=(map(evenodd,li))
# print(list(res))

# li =['apple','ball','is','email','gmail']
# string = lambda num: num if num[0] in "AEIOUaeiou" else '-'
#
#
# res=(map(string,li))
# print(list(res))


# uppercase
# li = ['A','C','e','f']
# upper = lambda num: num.upper() if num.islower() else num
#
#
#
# res=map(upper(li))
# print(res)


# li = ['abc', 'B', 'c', 'd']
#
#
# def upper(num):
#     if 'a' <= num <= 'z':
#         num = num.upper()
#         return num
#
#     return num
#
#
# res = (map(upper, li))
# print(list(res))

# li = [-1,-2,-3,3,4,5]
# def neg(num):
#     if num >= 0:
#         return num
#
#     return abs(num)
#
#
# res = (map(neg, li))
# print(list(res))

# # li = [1,2,3,3,4,5]
# # def power(num,i=0):
# #     num = num ** i
# #     i += 1
#     return num
#
# res = (map(power, li))
# print(list(res))

# length of character
# # s = "hello world how"
# # def string(num):
# #     return (num,len(num))
# #
# #
# # res=(map(string,s.split()))
# # print(list(res))
#
# s = "hello world how"
# li = s.split()
# res=map(len,li)
# print(list(res))




# word and ascii number
# li = ['a','A','C','b']
# def asc(num):
#     return (num,ord(num))
#
# res=(map(asc,li))
# print(list(res))

# li = 'hai'
# def asc(num):
#     return (num,ord(num))
#
# res=(map(asc,li))
# print(list(res))

# # power and indices
# l = [10,20,30,40]
# def func(item):
#     return item[1] ** item[0]
# res=(map(func,enumerate(l)))
# print(list(res))


# addition of 2 number
# a = [10,20,30,40]
# b = [2,6,7,8]
# def func(item1,item2):
#     return item1 + item2
# res=(map(func,a,b))
# print(list(res))

# even value in below list
# li = [1,2,3,4,5,6,7,8]
# def func(num):
#     if num % 2 == 0:
#         return num
# res=(filter(func,li))
# print(list(res))

# odd length
l = ['hai','hello','hell']
# def func(num):
#     if len(num) % 2 != 0:
#         return num
# res=(filter(func,l))
# print(list(res))

# op = lambda string:string if len(string) % 2 != 0 else '-'
# res = (map(op,l))
# print(list(res))



# sentence = 'hai hello how are you'
# def vowel(string):
#     if string[0] in "aeiouAEIOU":
#         return string
# res = (filter(vowel,sentence.split()))
# print(list(res))


# sentence = 'hai hello how are you'
# op = lambda string: string[0] in 'aeiouAEIOU'
# res = (filter(op, sentence.split()))
# print(list(res))

# length of each keyword
# s = "hai hello how are you"
# op = lambda string:(string,len(string))
# res = (map(op,s.split()))
# print(list(res))


