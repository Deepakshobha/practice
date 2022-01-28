""" palindrome"""
list_ = ["hai", "mom", "dad", "hello"]
palindrome = lambda string: f"{string} is a palindrome" if string == string[::-1] else "not a palindrome"

# for item in list_:
#     print(palindrome(item))

res = map(palindrome, list_)
# print(list(res))


""" even or odd """

l = [1, 2, 3, 4, 5, 6]

def evens(num):
    if num % 2 == 0:
        return f"{num} is even"
    return f"{num} is odd"

res = map(evens, l)
# print(list(res))

""" strings starting with vowels """
l = ["apple", "gmail", "yahoo", "flipkart"]

def vowels(item):
    if item[0] in "aeiouAEIOU":
        return item

res = map(vowels, l)
# print(list(res))

""" words into uppercase """

sentence = "hello world"

# def upper_(word):
#     return word.upper()
#
# upper_lambda = lambda word: word.upper()
# print(list(map(upper_lambda, sentence.split())))

res = map(str.upper, sentence.split())
# print(list(res))

res = map(str.lower, sentence.split())

""" all negative into positive numbers """

l = [1, 6, -3, 9, -3, -4, 1, -1]

# def convert_(num):
#     return abs(num)
#
# con = lambda num: abs(num)

# res = map(abs, l)
# print(list(res))

sentence = "hi good morning"
l = sentence.split()

res = map(len, l)
# print(list(res))


def word_len(word):
    return word, len(word)

res = map(word_len, l)
# print(list(res))

word = "hai"

def char_ascii(char):
    return char, ord(char)

res = map(char_ascii, word)
# print(list(res))

""" item to the power of its index"""
l = [10, 20, 30, 40]

def func(item):
    # index, item = item
    return item[1] ** item[0]

# for item in enumerate(l):
#     print(func(item[0], item[1]))

# map(func, enumerate(l))
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

def add_(item1, item2):
    return item1 + item2

res = map(add_, a, b)
# print(list(res))








































