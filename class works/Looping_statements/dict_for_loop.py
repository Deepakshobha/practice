""" print the keys in a dictionary """
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# # traversing through dictionary directly
# for key in d:
#     print(key, end=" ")
# print()
#
# # d.keys()
# for key in d.keys():
#     print(key, end=" ")
# print()
#
# # d.items()
# for key, value in d.items():
#     print(key, end=" ")

""" print only values in a dictionary """

# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# using dictionary[key]
# for key in d:
#     print(d[key], end=" ")
# print()
#
# # get()
# for key in d:
#     print(d.get(key), end=" ")
# print()
#
# # d.values()
# for value in d.values():
#     print(value, end=" ")
# print()
#
# # d.items()
# for key, value in d.items():
#     print(value, end=" ")

""" print items along with their indices"""
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
#
# # applying enumerate on dictionary variable
# for item in enumerate(d):
#     print(item, end=" ")
# print()
#
# # enumerate(d.items())
# for index, (key, value) in enumerate(d.items()):
#     print(index, key, value, end=" ", sep=" - ")

""" create a dictionary of character and its count"""

# string = "hello world"

# count()
# d = {}
# for char in set(string):
#     d[char] = string.count(char)
#
# print(d)

# without inbuilt method
# string = "hello world"
# d = {}
#
# for i in string:
#     count = 0
#     for j in string:
#         if i == j:
#             count += 1
#     d[i] = count
# print(d)

# using if else

# s = "hello world"
# d = {}

# for char in s:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
#
# print(d)

# from collections import defaultdict
# s = "hello world"
# dd = defaultdict(int)
# print(dd)
#
# for char in s:
#     dd[char] = dd[char] + 1
#
# print(dd)


""" word and its count pair """
sentence = "python is a language, python programming is easy"
d = {}
#
# # using count()
list_ = sentence.split()
for word in list_:
    d[word] = list_.count(word)

print(d)

# without using inbuilt method
sentence = "python is a language, python programming is easy"
list_ = sentence.split()
d = {}
#
# for word in list_:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)
#
# # using defaultdict
# from collections import defaultdict
#
# sentence = "python is a language, python programming is easy"
# dd = defaultdict(int)
# list_ = sentence.split()
#
# for word in list_:
#     dd[word] += 1
#
# print(dd)

""" word and its length pair """
# sentence = "python is a language, python programming is easy"
# list_ = sentence.split()
# d = {}
#
# for word in list_:
#     d[word] = len(word)
#
# print(d)

""" even length word and its length pair """
# sentence = "python is a language, python programming is easy"
# list_ = sentence.split()
# d = {}
#
# for word in list_:
#     if len(word) % 2 == 0:
#         d[word] = len(word)
#
# print(d)

""" word and length pair only if the word is starting with vowel """
# sentence = "python is a language, python programming is easy"
# list_ = sentence.split()
# d = {}
#
# for word in list_:
#     if word[0].lower() in "aeiou":
#         d[word] = len(word)
#
# print(d)

""" non repeated word and its count pair"""
# sentence = "python is a language, python programming is easy"
# list_ = sentence.split()
# d = {}
#
# for word in list_:
#     if list_.count(word) == 1:
#         d[word] = list_.count(word)
#
# print(d)

""" reverse the values in the dictionary if the value is of type string"""

# d = {"a": "hello", "b": 100, "c": 10.2, "d": "world"}
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
# print(d)

""" duplicate items and its count pair """

# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
# d = {}
#
# for name in names:
#     count = names.count(name)
#     if count > 1:
#         d[name] = count
# print(d)

""" """
sentence = "hello world welcome to python programming hi there"
op = {"h": ["hello", "hi"], "w": ["world", "welcome"], "t": ["to", "there"],
      "p": ["python", "programming"]}

# using normal dictionary
d = {}
list_ = sentence.split()

for word in list_:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]] += [word]
        # d[word[0]].append(word)

print(d)

# defaultdict

# from collections import defaultdict
#
# dd = defaultdict(list)
#
# for word in list_:
#     # dd[word[0]] += [word]
#     dd[word[0]].append(word)
#
# print(dd)

""" element and its indices pair """
# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
#
# # normal dictionary
# d = {}
#
# for index, item in enumerate(names):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
#
# print(d)
#
# # using defaultdict
# from collections import defaultdict
# dd = defaultdict(list)
# for index, item in enumerate(names):
#     dd[item] += [index]
#
# print(dd)

""" flip key and value """

# d = {"a": 1, "b": 2, "c": 3}
# d1 = {}
# for key in d:
#     value = d[key]
#     d1[value] = key
#
# print(d1)
# using d.items()
# d2 = {}
# for key, value in d.items():
#     d2[value] = key
#
# print(d2)

































































