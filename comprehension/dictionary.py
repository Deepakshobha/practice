# string = "hello"
# op = {item:index for index,item in enumerate(string)}
# print(op)

s = "hai hello"
r = s.split()
# d = {}
# for word in r:
#     d[word] = len(word)
# print(d)

# d1 = {word:len(word) for word in r}
# print(d1)

# count the character
s = "hai hello"
# d = {}
# count = 0
# for i in s:
#     d[i] = s.count(i)
# print(d)

# op = {i:s.count(i) for i in s}
# print(op)

# s = "hai hello"
# d = {}
# count = 0
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

# count the word
# s = "hai hello how are you hai hello"
# r = s.split()
# # d = {}
# # for i in r:
# #     d[i] = r.count(i)
# # print(d)
#
# op = {i:r.count(i) for i in r}
# print(op)

# count the word of even lengh
# s = "hi hell hell how are is  you hai hello"
# r = s.split()
# d = {}
# for i in r:
#     if len(i) % 2 == 0:
#         d[i] = r.count(i)
# print(d)

# op = {i:r.count(i) for i in r if len(i) % 2 == 0}
# print(op)

# s = "hi hello every one is"
# r = s.split()
# # d = {}
# # for index, item in enumerate(r):
# #     if len(item) % 2 != 0:
# #         d[index] = item[::-1]
# #     else:
# #         d[index] = item
# # print(d)
#
# op = { index:item if len(item) % 2 == 0 else item[::-1] for index,item in enumerate(r)}
# print(op)

# starting with vowel
# s = "hi hello every one is"
# r = s.split()
# op = {i:len(i) for i in s.split() if i[0] in "aeiouAEIOU"}
# print(op)

# index with datatype string reverse the data else keep as it is
# li = [1,12,1.3, "python", 'java',"c++",4+5j]
# op = {index:item[::-1] if isinstance(item,str) else item for index, item in enumerate(li)}
# print(op)

# index and word pair string keep as it is else reverse it
# s = ['hai', 'hello', 123, 4+5j]
# op = {index:item if isinstance(item,str) else str(item)[::-1] for index, item in enumerate(s)}
# print(op)

# d1 = {'a' = 123, 'b'=4+5j}
# op = {for index, item in enumerate(d1)}

# flip key and value
# d ={'a':1, 'b':2}
# op= {value:key for key,value in d.items()}
# print(op)

# deep unpacking
# d1 = {'a':123, 'b':4+5j, 'c':56}
# op = {index:value for index,value in enumerate(d1.items())}
# print(op)

# not repeated
# s = "python is a language to python is a"
# r = s.split()
# count = 1
# op = {i:count for i in r if r.count(i) == 1}
# print

# duplicate items how many times its repeated
# s = "python is a language to python is a python"
# r = s.split()
# print (r)
# count = 1
# op = {i:count for i in r if r.count(i) > 1}
# print(op)

# s = "python is a language to python is a python"
# r = s.split()
# d = {}
# count = 0
# for i in r:
#     if r.count(i) > 1:
#         count = r.count(i)
#         if count > 1:
#             d[i] = count
# print(d)

# s = "python is a language to python is a python"
# r = s.split()
# op = {i:r.count(i) for i in r if r.count(i) > 1}
# print(op)

# character and ascii pair(
# s = "PythoN "
# op = {i:ord(i) for i in s}
# print(op)

# s = "hello world welcome to hi python programming hi there"
# r = s.split()
# # d = {}
# # for i in r:
# #     if i[0] not in d:
# #         d[i[0]] = [i]
# #     else:
# #         d[i[0]] += [i]
# # print(d)
#
# op = {op[i[0]]:[i] if i[0] not in op  else (i) for i in r}
# print(op)
