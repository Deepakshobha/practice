# b = '(({[]})}'
# a = b[::-1]
# i = 0
# while i < len(b)//2:
#     if ord(a[i]) == ord(b[i]) + 1 or ord(a[i]) == ord(b[i]) + 2:
#         print(True)
#     else:
#         print(False)
#     i += 1
#
#
# d = {'1':True,'2':False,'3':True,'4':False}
# l = []
# for i in d:
#     if d[i] == True:
#         l.append(i)
#         d[i]='pass'
# print(l)
# print(d)

#count number of iterables
# def iterable(args):
#     count = 0
#     for _ in args:
#         count += 1
#     print(count)
#
# iterable({1,2,3,4,6})

#reverse string
# a ="Hello"
# i = 0
# st =""
# while i!= len(a):
#     st = a[i] + st
#     i += 1
# print(st)
#
# b = a[::-1]
# print(b)

#replace string
# a = "hello world"
# a=("hello world").replace("world","universe")
# print(a)

#comma separated string
# a = "hell world"
# b = a.split()
# print(b)
# c=','.join(b)
# print(c)


#alternate char
# a = "shobha"
# print(a[::2])

#upper to lower
a = "ShoBhA"
b = ''
for i in a:
    if 'A'<=i<='Z':
        b += chr(ord(i)+32)
    elif 'a'<=i<='z':
        b += chr(ord(i)-32)
    else:
        b += i
print(b)

#swap numbers
a,b = 1,2
b,a = a,b
print(a,b)

#merge 2 lists
# a = [1,2,3]
# b =[3,6,7]
# c = (*a,*b)
# print(c)

# sentence = "hello world welcome to python programming hi there"
# r =sentence.split()
# from collections import defaultdict
# d =defaultdict(int)
# for i in r:
#     if i[0] in d:
#         d[i[0]] += [i]
#     else:
#         d[i[0]] = [i]
# print(d)
#
# search chr find index
c = 'b'
a = "shobha"

for index,value in enumerate(a):
    if c == value:
        print(f"{value} of {index}")
