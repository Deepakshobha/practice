# def fac(n):
# 	if n == 1:
# 		return 1
# 	return n * fac(n-1)
# res = (fac(3))
# print(res)

	# 10 natural numbers
# for i in range(1,11):
#     print(i)
#
#
# def count_(start,end=0):
#     l = []
#     for i in range(start,end):
#         l.append(i)
#     print(l)
# count_(1,11)

# def count_(n):
#     if n <= 10:
#         print(n)
#         return count_(n+1)
# (count_(1))


#recursion from 1 to 10
# def num_(start,end):
#     if start<end:
#         print(start)
#         return num_(start+1,end)
# res = num_(1,11)
# print(res)


#recursion program to add digit of numbers
# num = 123
# a = str(num)
# i = 0
# sum = 0
# while i<=len(a)-1:
#     sum += int(a[i])
#     i += 1
# print(sum)

# def digit_(n,i=0,sum=0):
#     a = str(n)
#     if i<=len(a)-1:
#         sum += int(a[i])
#         print(sum)
#         return digit_(n,i+1,sum)
#
# digit_(123)



# def add_(a,b):
# 	print(a+b)
# add_(1,2)
#
#
# add_ = lambda a,b:a+b
# print(add_(1,2))
#
#
# even_ = lambda a: a%2 == 0
# print(even_(3))
#
# multi = lambda a, b:a*b
# print(multi(1,2))

# element = lambda *a : a[-1]
# print(element(1,2,3,4))

#
number_ = lambda n :f"{n} is even" if n % 2 == 0 else n+1
print(number_(3))
#



