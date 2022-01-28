""" add 2 numbers """

# positional and keyword arguments
def sum_(a, b):
    return a + b


# sum_(1, 2)
# sum_(a=1, b=2)

# positional only
def sum_(a, b, /):
    return a + b

# sum_(1, 2)

# keyword only
def sum_(*, a, b):
    return a + b
# sum_(a=1, b=2)

""" even numbers in the given range"""

def evens(end, start=0):
    l = []
    for i in range(start, end):
        if i % 2 == 0:
            l.append(i)
    return l

# print(evens(21))
# print(evens(21, 5))


""" prime numbers in the user defined range"""

def prime_(end, start=2):
    res = []

    for n in range(start, end+1):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                res.append(n)

    return res

# print(prime_(start=1, end=50))


""" """














