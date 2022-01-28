# def greet():
#     yield "hello world"
#     yield "hai"
#     yield "hello"
#
# msg = greet()
# print(list(msg))
#
# def greet():
#     yield "hello world"
#     yield "hai"
#     yield "hello"
#
# msg = greet()
# for item in msg:
#     print(item)
#
# l = [1,2,3,4]
# res = [item**2 for item in l]
# print(res)

# l = [1,2,3,4]
# def square(*args):
#     for i in args:
#         yield i**2
#
# re = (square(*l))
# print(list(re))


# l = [1,2,3,4]
# def square(*args):
#     for i in args:
#         yield i**2
#
# re = (square(*l))
# for item in re:
#     print(item)


l = [1,2,3,4]
# def square(*args):
#     for i in args:
#         yield i**2
#
# re = (item**2 for item in l) # generator expression its not a comprahension
# for item in re:
#     print(item)
# #
#
#
# l = [1,2,3,4]
# def square(*args):
#     for i in args:
#         yield i**2
#
# re = (item**2 for item in l) # generator expression its not a comprahension
#
# print(re)
# print(next(re))
# print(next(re))
# print(next(re))
# print(next(re))



# even numbers in 1-50 using generator function
# def evens():
#     for item in range(1,51):
#         if item%2 == 0:
#             yield item
# res=evens() #generator object
# print(list(res))


# even numbers in 1-50 using generator function
# def evens():
#     for item in range(1,51):
#         if item%2 == 0:
#             yield item
# res=(item for item in range(1,51) if item % 2 == 0)
# print(list(res))


# starting with vowel in given list:
#
# l =['john','apple','union','ball']
#
# def vowel(*args):
#     for item in args:
#         if item[0] in "aeiouAEIOU":
#             yield item
#
# res = vowel(*l)
# print(list(res))


# l =['john','apple','union','ball']
#
# def vowel(*args):
#     for item in args:
#         if item[0] in "aeiouAEIOU":
#             yield item
#
# res = (item for item in l if item[0] in "aeiouAEIOU")
# print(list(res))

#to yield length of each line in a file only if the line is not empty

# path = r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.txt"
# def files():
#     with open(path) as file1:
#         for line in file1:
#             if line.strip():
#                 yield line,len(line)
# res =files()
# print(list(res))

#
# path = r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.txt"
# with open(path) as file1:
#     def files():
#         for line in file1:
#             if line.strip():
#                 yield line,len(line)
#     res =((line,len(line)) for line in file1 if line.strip())
#     print(list(res))
#
#

# names =['john','apple','union','ball']
# d = {}
# for name in names:
#     d[name] = len(name)
# print(d)

# names =['john','apple','union','ball']
# d = {}
# for name in names:
#     if name[0] not in d:
#         d[name[0]] = [name]
#     else:
#         d[name[0]] += [name]
# print(d)

# #try except""
# names =['john','apple','union','ball']
# d = {}
# for name in names:
#     try:
#         d[name[0]] += [name]
#     except:
#         print("in except block")
# print(d)

#default exception block
# a = 10
# b = 0
# try:
#     print(a/b)
#     print(l.append(10))
#
# except:
#     print("hello")


# a = 10
# b = 0
# try:
#     print(a/b)
#     # print(l.append(10))
#
# except NameError:
#     print("hello")


# a = 10
# b = 0
# try:
#     print(a/b)
#     print(l.append(10))
#
# except:
#     print("hello")

#multiple expo
a = 10
b = 0
try:
    print(a/c)
    print(l.append(10))

except ZeroDivisionError:
    print("zero division hnadled")
except NameError:
    print("name error")
finally:
    print('hello')
#
#
#
# # a = 10
# # b = 0
# # try:
# #     # print(a/b)
# #     print(l.append(10))
# #
# # except (ZeroDivisionError,NameError) as error_msg: # error_msg catches the error occur in except block
# #     print('IN except block')
# #     print(error_msg)
#
#
# # a = 10
# # b = 0
# # try:
# #     # print(a/b)
# #     print(l.append(10))
# #
# # except as error_msg: # not possible
# #     print('IN except block')
# #     print(error_msg)
#
#
# # BaseException --> Exception -->all other exception
# # a = 10
# # b = 0
# # try:
# #     # print(a/b)
# #     print(l.append(10))
# #
# # except BaseException as error_msg:
# #     print('IN except block')
# #     print(error_msg)
#
#
#
#
# class UsernotauthorisedExeception(Exception):
#     pass
#
# username = "shobh"
# password = 123
#
# try:
#     if username == 'shobha':
#         print("user name is matched")
#     else:
#         raise UsernotauthorisedExeception("user not present")
#
# except BaseException as error_msg:
#     print('IN except block')
#     print(error_msg)
# else:
#     print('in home page')
#
# finally:
#     print("closing the browser")
#
#
#
# username = "shobha"
# password = 123
#
# try:
#     if username == 'shobha':
#         print("user name is matched")
#     else:
#         raise NameError("user not present")
#
# except NameError:
#     pass
# else:
#     print('in home page')
#
# finally:
#     print("closing the browser")