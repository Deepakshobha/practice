# 1 count the character
s = "hello world"
d = {}

for char in s:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1

# print(d)

# 2 indexes of below item
li = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
d = {}

for index,item in enumerate(li):
    if item not in d:
        d[item] = [index]
    else:
        d[item] += [index]
# print(d)

# 3 grouping of extension
s = ['apple.com','ball.in','ball.in','cat.com','apple.net','apple.net']
l = []
d = {}
for i in s:
    r = i.split('.')
    if r[1] in d:
        d[r[1]] += [i]
    else:
        d[r[1]] = [i]
# print(d)

# 4 count the repeated character
from collections import defaultdict
s = 'haihellowhowareyou'
dd = defaultdict(int)
for i in s:
        if s.count(i) > 1:
            dd[i] = s.count(i)
# print(dd)

# 5 reverse the value in the dict if value str
d = {'a':'hello','b':12,'c':'world'}
for key,value in d.items():
    if isinstance(value,str):
        d[key] = value[::-1]
# print(d)

# 6 how many times its repeated
li = ['apple','ball','apple','apple','cat','ball']
d = {}
for i in li:
    if li.count(i) > 1:
        d[i] = li.count(i)
# print(d)

#7 grouping of flowers and animals
li = ['lotus-flower','rose-flower','cat-animal','dog-animal','jasmine-flower']
d = {}
for i in li:
    r = i.split('-')
    if r[1] not in d:
        d[r[1]] = [i]
    else:
        d[r[1]] += [i]
# print(d)


# 8  grouping even and odd
from collections import defaultdict
li = [1,2,3,4,5,6,7,8,9]
d = defaultdict(list)
for i in li:
    if i % 2 == 0:
        d[0] += [i]
    else:
        d[1] += [i]
# print(d)

# 9 grouping
from itertools import zip_longest
cities = ['bangalore','mysore','delhi','newyork']
population = [111,121,321]
d ={}
for c,p in zip_longest(cities,population):
    d[c] = p
# print(d)

# 10 flip keys and values
d = {"a": 1, "b": 2, "c": 3}
d1 = {}
for key in d:
    value = d[key]
    d1[value] = key

print(d1)
using d.items()
d2 = {}
for key, value in d.items():
    d2[value] = key

print(d2)

