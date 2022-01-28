# 1 word and count pair using dict
# sentence = "it is very gud book reading is a gud habit"
# r = sentence.split()
# d ={}
# def count(*args):
#         for i in args:
#             if i not in d:
#                 d[i] = 1
#             else:
#                 d[i] += 1
#         return d
# res=(map(count,r))
# print(list(res))

# 2 count number of elements in list without using inbuilt
# a=['hai','hello','how','are','you']

# def count_(*args):
#     count = 0
#     for i in args:
#         count += 1
#     return count
# print(count_(*a))
#
#
# # 3 starting with vowels
# sentence = "it is very gud book reading is a gud habit"
# r = sentence.split()
# def count(*args):
#         for i in args:
#             if i[0] in 'aeiouAEIOU':
#               return i
# res=(filter(count,r))
# print(list(res))

# 4 prime
# def prime(n):
#     for i in range(2,n):
#         if n%2 == 0:
#             return f"{n} not prime"
#         return f"{n} is prime"
# print(prime(3))


# 5 fiboo
# l =[]
# def fib(n):
#     a = 0
#     b = 1
#     i = 0
#     while i <= n:
#         l.append(a)
#         c = a+b
#         a = b
#         b = c
#     print(l)
# fib(10)



# 6 def string(*args):
#     for i in args:
#         return i[::-1]
# print(string('shobha'))

# 7 prime
# def prime(n):
#     for i in (2,n):
#         if n%i == 0:
#             return (n+1)
#         return n
# print(prime(11))

# 8 upper to lower and lower to upper
# s = "Hai HellO HOW aRE You"
# st1 = ''
# def string(num):
#   st = ""
#
#   for i in num:
#       if 'a'<=i<='z':
#           st += chr(ord(i)-32)
#       elif 'A'<=i<='Z':
#           st += chr(ord(i) + 32)
#       else:
#           st += i
#       return st
# res=(map(string,s))
# b = tuple(res)
# for j in b:
#     st1 += j
# print(st1)

# 1st last middle cha in string
string = "to get all the notifications about upcoming videos"
b = len(string)//2
f = string[0]
l = string[-1]
print(b)
m2 =string[b]+string[b+1]
print(f,l,m2)









