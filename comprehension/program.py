# l =[1, 2, 3, 4, 5]
# li = []
# for i in l:
#     li.append(i**2)
# print(li)

# list of tuples
# l =[1, 2, 3, 4, 5]
# li = []
# for item in enumerate(l):
#     li.append((item))
# print(li)

# l =[1, 2, 3, 4, 5]
# op = [(item) for item in enumerate(l)]
# print(op)


# l =[1, 2, 3, 4, 5]
# op = [(index,item) for index, item in enumerate(l)]
# print(op)

# li = list(range(10))
# op = [item for item in li if item % 2 == 0]
# print(op)

# odd an even
# li = list(range(10))
# odd = [item for item in li if item % 2 != 0]
# even = [item for item in li if item % 2 == 0]
# print(odd, even)

# even lengh save as it is odd lengh reverse and store
# li = ['python', 'java', 'selium', 'abc', 'abcde']
# l = []
# for i in li:
#     if len(i) % 2 == 0:
#         l.append(i)
#     else:
#         l.append(i[::-1])
# print(l)

# li = ['python', 'java', 'selium', 'abc', 'abcde']
# res = [item if len(item) % 2 == 0 else item[::-1] for item in li]
# print(res)

# string keep as it is else revese it

# li = ['java', 'python', 10, True, 1.4, "c++", "ruby"]
# l = []
# for i in li:
#     if isinstance(i,str):
#         l.append(i)
#     else:
#         i = str(i)
#         l.append(i[::-1])
# print(l)

# output = [str(item)[::-1] if not isinstance(item,str) else item for item in li]
# print(output)

#
# li = ['amazon.com', 'walmart.in', 'email.net']
# l = []
# for i in li:
#     a = i.split('.')
#     print(l.extend(a))


# li = [10,20,10,40,20]
# b = 10
# for index, item in enumerate(li):
#     if item == b:
#         print(item,index)
#         break
# else:
#     print('element not present')


# li = "shobhas"
# b = 's'
# flag = 0
# for index, item in enumerate(li):
#     if item == b:
#         print((index,item),end ='')
#         flag += 1
# if flag == 0:
#     print('element not present')


# l = ['mom','python','dad']
# res = set()
# for i in l:
#     if i == i[::-1]:
#         res.update([i])
# print(res)




