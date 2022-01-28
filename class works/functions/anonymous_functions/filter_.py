""" even values in the list"""

l = [1, 2, 3, 4, 5, 6, 7, 8]

def even(num):
    if num % 2 == 0:
        return num


# evens = filter(even, l)
# print(list(evens))

""" list of strings with odd length """

l = ["gmail", "flipkart", "google", "yahoo", "rediff"]

def odd_(string):
    if len(string) % 2 != 0:
        return string * 2

# odd_2 = lambda string: len(string) % 2 != 0

odd_len = filter(odd_, l)
# print(list(odd_len))


""" words starting with vowels in the sentence """
sentence = "hello hai how are you"

l = [1, 2, 3, 4, 5, 6, 7, 8]

# def squares(item):
#     if item % 2 == 0:
#         return item ** 2


# numbers = list(filter(squares, enumerate(l)))
# res = map(squares, numbers)
# print(list(res))















