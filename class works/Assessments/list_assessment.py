""" remove all the duplicate elements """

l = ["a", "b", "c", "d", "b", "c"]
res = []
for item in l:
    if l.count(item) == 1:
        res.append(item)    # ["a", "d"]
# print(res)

# not in
res = []
for item in l:
    if item not in res:
        res.append(item)
# print(res)

# set()
# print(list(set(l)))

""" print numeric value in the list """

items = ["python", 1.2, 9, 1 + 2j, [1, 2, 3], True]

# for item in items:
#     if isinstance(item, (int, float, complex)):
#         print(item)

""" sum of all even numbers in the string """
string = "alpha3python127 selenium12,47956"
evens = 0

for char in string:
    if "0" <= char <= "9" and int(char) % 2 == 0:
            evens += int(char)

# print(evens)

""" create a set of languages starting with "p" """

languages = ["python", "java", "Perl", "PHP", "Python"]
s = set()

for item in languages:
    if item[0] in "pP": # if item[0].lower() in "p":
        s.add(item)

# print(s)

""" list with only even length string """

languages = ["python", "java", "Perl", "PHP", "Python"]
res = []

for item in languages:
    if len(item) % 2 == 0:
        res.append(item)

# print(res)

""" reverse if odd length else keep it as it is """

languages = ["python", "java", "Perl", "PHP", "Python", "c++", "node JS"]

# for item in languages:
#     if len(item) % 2 == 0:
#         print(item)
#     else:
#         print(item[::-1])

""" sum of entire list and sum of internal list"""

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
entire_sum = 0

for item in l:      # [1, 2, 3], [4, 5, 6]
    internal_sum = 0
    for i in item:          # (1, 2, 3), (4, 5, 6)
        internal_sum += i
        entire_sum += i     # 0+1= 1, 1+2= 3, 3+3=6, 6+4=10, 10+5=15, 15+6= 21
#     print(internal_sum)
# print(entire_sum)   # 6

""" list of prime numbers"""

prime_ = []

for n in range(1, 101):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            prime_.append(n)
# print(prime_)

""" reverse the list """

l = ["hi", "hello", "python"]
res = []

for item in l[::-1]:
    res.append(item[::-1])

# print(res)

""" rotating the list based on k value """

languages = ["python", "java", "Perl", "PHP", "Python"]
k = 4

for i in range(k):
    item = languages.pop()
    languages.insert(0, item)
# print(languages)

















































