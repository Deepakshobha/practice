
l =["mom","dad","apple"]
pali = lambda a:f"{a} is palindrome" if a == a[::-1] else a*3
res= map(pali,l)
print(res)
print(list(res))

#normal function
# l =["mom","dad","apple"]
# def pali(args):
#     if args == args[::-1]:
#         return "palindrome"
#     else:
#         return "no palindrome"
#
#
# res = map(pali,l)
# print(list(res))
#
# #addition
# a=[1,2,3,4]
# b= [4,5,6,7,9]
#
# def add_(n,m):
#      return n+m
#
# res = map(add_,a,b)
# print(list(res))
#
#
# #
# l = ["hai","hello","java"]
# # def odd_(a):
# #     if len(a)%2 == 0:
# #         return a
# # res = (filter(odd_,l))
# # print(list(res))
#
# #
# #
# # Output = map(lambda x:x+3, [1,2,3,4])
# # print(list(Output))
#
# l = [1,2,3,4,5]
# # output = lambda a:f"{a} is even" if a%2 == 0 else f"{a} is odd"
# # res= map(output,l)
# # print(list (res))
#
#
# def num_(args):
#     if args%2 == 0:
#         return args
#     res = filter(num_,l)
# print(list(res))
