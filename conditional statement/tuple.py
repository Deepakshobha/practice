# # Write a program to print a tuple of character and its ascii value in the given string
# s = "hello world"
# p = ()
# for i in s:
#     t = ord(i)
#     p += ((i,t))
# print(p)
# Write a program to print a tuple of character and its ascii value in the given string
# n = 5
# for i in range(2,n):
#     if n % i == 0:
#         print("not prime")
# else:
#     print("prime")

# Write a program to print the sum of all the digits present inside the string
# s ="1234stuv999"
# sum = 0
# for i in s:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

# s ="1234stuv"
# sum = 0
# for i in s:
#     if '0' <= i <= '9':
#         sum += int(i)
# print(sum)

#  WAP to print all the consonants present in the sting
# along with total coun
# s = "abcdefghij"
# f =[]
# count = 0
# for i in s:
#     if i in "aeiouAEIOU":
#         pass
#     else:
#         count += 1
#         f.append(i)
# print(f,count, sep ="-")

#
# s = "aeioubcdef"
# count = 0
# for item in s:
#
#
# # tuple of index and char in string
# s = "shobha"
# for index, item in enumerate(s):
#     print((index,item))

# s = "shobha"
# for i in range(len(s)):
#     print((s[i],i))
# wap to reverse a string 3 ways
# s = "shobha"
# for i in reversed(s):
#     print(i, end="")
# s = "shobha"
# for i in s[::-1]:
#     print(i, end='')
# only spl from string
s = "#@*123abc"
# for i in s:
#     if i.isdigit() or i.isalpha():
#         pass
#     else:
#         print(i, end="")
# wap if the given character present in the if char present written its index

s = "shobhab"
t = 'b'
f = 0
for i in range(len(s)):
    if t == s[i]:
        f += 1
        print((t, i))
if f == 0:
    print("char not present")
else:
    print(f)




