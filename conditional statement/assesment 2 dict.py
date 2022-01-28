# 1 indexes of below item
li = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
d = {}

for index,item in enumerate(li):
    if item not in d:
        d[item] = [index]
    else:
        d[item] += [index]
# print(d)

# 2 reverse the value in the dict if value str
d = {'a':'hello','b':12,'c':'world'}
for key,value in d.items():
    if isinstance(value,str):
        d[key] = value[::-1]
# print(d)

# 3 duplicate how many times its repeated
li = ['apple','ball','apple','apple','cat','ball']
d = {}
for i in li:
    if li.count(i) > 1:
        d[i] = li.count(i)
# print(d)

# 4 maping using dict coprahnension
from itertools import zip_longest
cities = ['bangalore','mysore','delhi','newyork']
population = [111,121,321]
# d ={}
# for c,p in zip_longest(cities,population):
#     d[c] = p
# print(d)

op = {c:p for c,p in zip(cities,population)}
print(op)

# 5 flip keys and values
d = {"a": 1, "b": 2, "c": 3}
d1 = {}
for key in d:
    value = d[key]
    d1[value] = key

# print(d1)
# using d.items()
d2 = {}
for key, value in d.items():
    d2[value] = key

# print(d2)

# 6  grouping even and odd indexces
from collections import defaultdict
li = [1,2,3,4,5,6,7,8,9,11,34,51,32]
d = defaultdict(list)
for index,value in enumerate(li):
    if index % 2 == 0:
        d[1] += [value]
    else:
        d[0] += [value]
print(d)

7