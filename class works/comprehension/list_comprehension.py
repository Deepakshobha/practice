# """ WAP to create a list of squares for the elements in the below list"""
# l = [1, 2, 3, 4, 5]
#
# # normal method
# res = []
# for i in l:
#     res.append(i ** 2)
#
# print(res)
#
# res = [i ** 2 for i in l]
# print(res)

#############################################
# l = [1, 2, 3, 4, 5]
#
# op = [item for item in l]
# print(op)

""" create list of tuples of index and its corresponding item in the list """
l = ["python", 10, 3.2, "selenium_", "Java"]

# normal method
l_index = []

for item in enumerate(l):
    l_index.append(item)

print(l_index)

# comprehension

l_index = [(index, item) for index, item in enumerate(l)]
print(l_index)

# l_index = [item for item in enumerate(l)]
# print(l_index)


""" list of even numbers """
l = list(range(10))

# normal
evens = []
for item in l:
    if item % 2 == 0:
        evens.append(item)
# print(evens)

# comprehension
evens = [item for item in l if item % 2 == 0]
# print(evens)

""" list of even and odd """
# l = list(range(10))
# evens = []
# odd = []
#
# for item in l:
#     if item % 2 == 0:
#         evens.append(item)
#     else:
#         odd.append(item)
# print(evens, odd)

# comprehension
# l = list(range(10))
# evens = [i for i in l if i % 2 == 0]
# odd = [i for i in l if i % 2 != 0]

""" if even store as it is else reverse and store it """
l = ["python", "Node JS", "selenium_", "Java"]

# normal
res = []
for item in l:
    if len(item) % 2 == 0:
        res.append(item)
    else:
        res.append(item[::-1])
# print(res)

# comprehension
# true if condition else false

res = [item if len(item) % 2 == 0 else item[::-1] for item in l]
# print(res)

""" reverse if it is a string else keep it as it is """
list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
output = []

# normal
for item in list_:
    if not isinstance(item, str):
        output.append(str(item)[::-1])
    else:
        output.append(item)

# print(output)

# comprehension
output = [str(item)[::-1] if not isinstance(item, str) else item for item in list_]
# print(output)

""" list of words starting with vowel """
files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo"]

vowels = [file for file in files if file[0].lower() in "aeiou"]
# print(vowels)











