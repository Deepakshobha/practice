# default sorting the collection data types
s = "hello"
# print(sorted(s))

l = [5, 4, 8, 6, 1, 9, 11, 7]
# print(sorted(l))

l = ["python", "java", "c", "ruby", "perl"]
# print(sorted(l))

t = ("python", "java", "c", "ruby", "perl")
# print(sorted(t))

set_ = {"python", "java", "c", "ruby", "perl"}
# print(sorted(set_))

d = {"gmail": 5, "apple": 3, "walmart": 7, "flipkart": 8}
# print(sorted(d, reverse=True))
# print(sorted(d.items()))


# custom sorting

# sorting based on the length of the elements
l = ["python", "java", "c", "ruby", "perl"]
# print(sorted(l, key=len))   # ascending order
# print(sorted(l, key=len, reverse=True))     # descending order

# longest and shortest words
sentence = "python is a programming language"
words = sentence.split()
shortest, *rest, longest = sorted(words, key=len)
# print((longest, len(longest)), (shortest, len(shortest)))

# based on last element of each element
l = ["python", "java", "c", "ruby", "perl"]

def last_item(ele):
    return ele[-1]

# print(sorted(l, key=last_item))

# using lambda
# print(sorted(l, key=lambda item: item[-1]))

# based on middle character of each element
l = ["python", "java", "c", "ruby", "perl"]
# print(sorted(l, key=lambda item: item[len(item)//2]))

# sorting dictionaries
# sorting a dictionary based on its keys

d = {"gmail": 5, "walmart": 7, "apple": 3, "flipkart": 8}

# # ASCII values
# print(sorted(d))    # ['apple', 'flipkart', 'gmail', 'walmart']
# print(sorted(d.keys())) # ['apple', 'flipkart', 'gmail', 'walmart']
# print(sorted(d.items()))    # [('apple', 3), ('flipkart', 8), ('gmail', 5), ('walmart', 7)]

# based on length of keys
# print(sorted(d, key=len))   # ['gmail', 'apple', 'walmart', 'flipkart']
# print(sorted(d.keys(), key=len))
# print(dict(sorted(d.items(), key=lambda item: len(item[0]))))

d = {"gmail": 5, "walmart": 1, "apple": 3, "flipkart": 8}

# based on values

# print(sorted(d, key=lambda item: d[item]))
# print(sorted(d.values()))
# print(dict(sorted(d.items(), key=lambda item: item[-1])))

temperatures = [("Delhi", 32), ("Mumbai", 27), ("Kolkata", 30), ("Chennai", 35)]

# print(sorted(temperatures, key=lambda item: item[-1]))

""" moat occurring word """
sentence = "hi how are you how is your health"
list_ = sentence.split()

d_count = {word: list_.count(word) for word in list_}
# print(d_count)
res = sorted(d_count.items(), key=lambda item: item[-1])
# print(res[-1])

""" longest word along with its length """
sentence = "python is a programming language and programming is fun"
list_words = sentence.split()

d = {item: len(item) for item in list_words}
print(d)
res = sorted(d.items(), key=lambda item: item[-1])
print(res[-1])

""" longest non repeated word along with its length """

sentence = "python is a programming language and programming is fun"
list_words = sentence.split()

d = {item: len(item) for item in list_words if list_words.count(item) == 1}
# print(d)
res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])

l = [{"name": "Ram", "class": 6, "age": 12},
     {"name": "Shyam", "class": 12, "age": 18},
     {"name": "John", "class": 8, "age": 13}]

# sort the above list based on the names
print(sorted(l, key=lambda item: item["name"]))

# sort the above list based on class
print(sorted(l, key=lambda item: item["class"]))

# sort the above list based on age
print(sorted(l, key=lambda item: item["age"]))



























































