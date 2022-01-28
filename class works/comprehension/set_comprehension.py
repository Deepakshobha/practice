""" set comprehension to create a set of squares from 1 to 10"""

res = set()
for i in range(1, 11):
    res.add(i ** 2)
# print(res)

res = {i ** 2 for i in range(1, 11)}
# print(res)

""" set of tuples with index and item """
list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]

res = {(item, list_[item]) for item in range(len(list_))}
# print(res)

res1 = {(index, item) for index, item in enumerate(list_)}
# print(res1)

""" set of tuples with item and its length pair """
files = ("Amazon", "flipkart", "walmart", "gmail", "yahoo")

set_ = {(item, len(item)) for item in files}
print(set_)















