# def count(n):
#     if n >= 1:
#         print(n)
#         n -= 1
#         count(n)
#     else:
#         return
# count(10)

# add = 0
# def count(n):
#     if i <= n
#         add = n
#         n += 1
#         count(n)
#     else:
#         return
# count(3)

# addition

# def add_(n,sum=0):
#     if n > 0:
#         last = n % 10
#         sum += last
#         n = n//10
#         return add_(n,sum)
#     else:
#         return sum
#
# add_(123)

# sum
# def add_(n,sum=0):
#     if n > 0:
#         sum += n
#         n -= 1
#         return add_(n,sum)
#     else:
#         return sum

# print(add_(5))
#
# factorial
# def fact_(n,ref=1):
#     if n > 0:
#         ref *= n
#         n -= 1
#         return fact_(n,ref)
#     else:
#         return ref
#
# print(fact_(5))



# def add_(n,count=0):
#     if n > 0:
#         count += 1
#         n = n//10
#         return add_(n,count)
#     else:
#         return count
#
# print(add_(1235))

# def add_(n):
#     if n:
#         return n[::-1]
#     return n
#
# print(add_("hai"))


def fib(n,i=0,a=0,b=1):
     if i < n:
        print(a)
        c = a+b
        a = b
        b = c
        i += 1
        return fib(n,i,a,b)
     return a

(fib(10))

