""
""" traversing through sets """

# set_ = {"python", "dad", "hai", "malayalam", "madam", "mom"}
#
# for item in set_:
#     print(item)


""" remove the element from the set """

set_ = {"python", "dad", "hai", "malayalam", "madam", "mom"}
key = "hai"

for ele in set_:
    if ele == key:
        set_.discard(key)
        break

# print(set_)

""" WAP to create a set with list elements if the element is palindrome"""

list_ = ["python", "dad", "hai", "malayalam", "madam", "mom"]
res = set()

for item in list_:
    if item == item[::-1]:
        res.add(item)

# print(res)






