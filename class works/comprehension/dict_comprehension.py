""" WAP to create a dictionary with item and its index pair"""

# normal method
string = "hello"
d = {}

for index, item in enumerate(string):
    d[item] = index
# print(d)

# comprehension

dict_ = {item: index for index, item in enumerate(string)}
# print(dict_)

""" WAP to create a dictionary with word and its length pair"""
sentence = "hello world welcome to python"
words = sentence.split()
d = {}

for word in words:
    d[word] = len(word)

# print(d)

# comprehension
d1 = {word: len(word) for word in words}
# print(d1)

""" create a dictionary of character and its count"""
s = "hello world"
d = {}

# normal method
for char in s:
    d[char] = s.count(char)
# print(d)

# comprehension
d1 = {char: s.count(char) for char in s}
# print(d1)

""" create a dictionary of word and its count"""
sentence = "python is a language, python programming is easy"
words = sentence.split()
d = {}

# normal method
for word in words:
    d[word] = words.count(word)
# print(d)

# comprehension

d = {word: words.count(word) for word in words}
# print(d)

""" dictionary with word and its count pair only if the word is of even length"""

sentence = "python is a language, python programming is easy"
words = sentence.split()

# normal method
d ={}
for word in words:
    if len(word) % 2 == 0:
        d[word] = words.count(word)
# print(d)

# comprehension

dd = {word: words.count(word) for word in words if len(word) % 2 == 0}
# print(dd)

""" dictionary with index and word pair if the word is of odd length reverse it,
else keep it as is"""

sentence = "python is a language, python programming is easy"
words = sentence.split()
d = {}

for index, word in enumerate(words):
    if len(word) % 2 == 0:
        d[index] = word
    else:
        d[index] = word[::-1]
# print(d)


dd = {index: word if len(word) % 2 == 0 else word[::-1] for index, word in enumerate(words)}
# print(dd)

""" word and length pair only if the word is starting with vowel """

sentence = "python is a language, python programming is easy"
words = sentence.split()

d = {word: len(word) for word in words if word[0].lower() in "aeiou"}
# print(d)

""" index and word pair if word is of type string reverse it """
list_ = ["python", 17, 9, "java", 19.9, 4+0j, "ruby", "c++"]

d = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(list_)}
# print(d)

""" index and word pair if word is of type string keep it as it else reverse it """
list_ = ["python", 17, 9, "java", 19.9, 4+0j, "ruby", "c++"]

d1 = {index: item if isinstance(item, str) else str(item)[::-1] for index, item in enumerate(list_)}
# print(d1)


d1 = {index: str(item)[::-1] if not isinstance(item, str) else item for index, item in enumerate(list_)}
# print(d1)

""" flip keys and values in a dictionary """
dict_ = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

res = {dict_[key]: key for key in dict_}
# print(res)

res = {value: key for key, value in dict_.items()}
# print(res)

""" char and ascii value pair """
# string = "python"

# d = {char: ord(char) for char in string}
# print(d)


















