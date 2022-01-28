l = ["python", 10, 3.2, "selenium_", "Java"]

""" traversing through list """

for item in l:
    print(item, end=" ")

print()
#
# for i in range(len(l)):
#     print(l[i], end=" ")


""" print index and its corresponding item in the list """
# l = ["python", 10, 3.2, "selenium_", "Java"]

# for i in range(len(l)):
#     print("index is:", i)
#     print("element is:", l[i])


# for index, item in enumerate(l):
#     print(index, item)

""" traversing through a list in reversed order """

# l = ["python", 10, 3.2, "selenium_", "Java"]

# # using range
# for i in range(len(l)-1, -1, -1):
#     print(l[i], end=" ")
#
# print()
# # using slicing
# for i in l[::-1]:
#     print(i, end=" ")
#
# print()
# # using reversed()
# for i in reversed(l):
#     print(i, end=" ")

""" print even indexed elements in the list """

# l = ["python", 10, 3.2, "selenium_", "Java"]
#
# # using range
#
# for i in range(0, len(l), 2):
#     print(l[i], end=" ")
# print()
#
# # using slicing
# for i in l[::2]:
#     print(i, end=" ")
# print()
#
# # using condition
# for i in range(len(l)):
#     if i % 2 == 0:
#         print(l[i])

""" print integers in a list """

# l = ["python", 10, 3.2, "selenium_", "Java"]
#
# for item in l:
#     if isinstance(item, int):
#         print(item)

""" print only numeric datatypes"""

# l = ["python", 10, 3.2, "selenium_", "Java"]

# for i in l:
#     if isinstance(i, (int, float, complex)):
#         print(i)

""" print length of each string in the list """

# l = ["python", "Node JS", "selenium_", "Java"]

# for item in l:
#     print((item, len(item)))

""" print the strings with even length """

# l = ["python", "Node JS", "selenium_", "Java"]
# res = []
# for item in l:
#     if len(item) % 2 == 0:
#         res.append(item)
#     else:
#         res.append(item[::-1])

# print(res)

""" reverse string elements or else keep it as it is"""

# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
# res = []
# for item in list_:
#     if isinstance(item, str):
#         res.append(item[::-1])
#     else:
#         res.append(item)

# print(res)

""" print if the element is starting with vowel """

# files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo"]

# for ele in files:
#     if ele[0].lower() in "aeiou":
#         print(ele)

""" print all the extensions in the following list """

# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]

# for file in files:
#     a = file.split(".")
#     print(a[-1])

""" printing file name with odd length """

# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]

# for item in files:
#     a = item.split(".")
#     if len(a[0]) % 2 == 0:
#         pass
#     else:
#         print(a[0])

""" index of first occurrence of the given element in the list"""

# numbers = [10, 40, 20, 80, 20, 40, 30]
# num = 60

# for index, item in enumerate(numbers):
#     if item == num:
#         print(f"{num} is present at the index {index}")
#         break
#
# else:
#     print("element is not present")

""" check if the number is a prime number """

# n = 15

# for i in range(2, n):
#     if n % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

""" to generate prime number series"""
# l = [1, 5, 8, 6, 3, 98, 12, 5]

# for n in range(10):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             print(n)

""" print the elements other than the given element"""
# numbers = [10, 40, 20, 80, 20, 40, 30]
# n = 20
#
# for num in numbers:
#     if n == num:
#         continue
#     print(num)

""" print the palindromes in the given list """
l = ["python", "dad", "hai", "malayalam", "madam", "mom"]

# for element in l:
#     if element == element[::-1]:
#         print(element)













