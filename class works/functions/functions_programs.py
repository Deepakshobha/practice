""" check if the number is prime or not"""
def is_prime(num):

    for i in range(2, num):
        if num % i == 0:
            return f"{num} is not prime"
    return f"{num} is a prime"

# print(is_prime(5))
# print(is_prime(10))

""" to return last digit of an integer """

def last_digit(num):
    return num % 10     # return str(num)[-1]


""" return last n elements from the sequence """

def tail(sequence, n):
    return sequence[-n:]

print(tail("hello", 2))
print(tail("hello", 4))

""" square or not"""

def is_perfect_sqaure(num):
    sq = int(num ** 0.5)
    if sq ** 2 == num:
        return True
    return False

# print(is_perfect_sqaure(27))

def is_perfect_sqaure(num):

    for i in range(num):
        if i * i == num:
            return True
    return False


# print(is_perfect_sqaure(2))

""" func("TRACXN", 0)   # should print RCN
    func("TRACXN", 1)   # should print TAX"""

def func(string, n):
    if n == 0:
        return string[1::2]
    elif n == 1:
        return string[::2]
    else:
        return "n value is invalid"

# print(func("TRACXN", 2))


""" check if the number is fibonocci number or not"""

def is_fibo(num):
    a = 0
    b = 1
    while a <= num:
        if a == num:
            return f"{num} is a fibonacci number"
        c = a + b
        a = b
        b = c
    return f"{num} is not a fibonacci number"


# is_fibo(0)

""" length of iterables """
def iterable_length(*args):
    for item in args:
        if isinstance(item, (str, tuple, list, set, dict)):
            print(item, len(item))


# iterable_length(1, "hello", (1, 2, 3), 19.5, 1 +4j)


def squares(n):
    i = 0
    l = []
    while i <= n:
        sq = int(i ** 0.5)
        if sq * sq == i:
            l.append(i)
        i += 1

    return l
# print(squares(10))

def spam(name="steve"):
    print(name)

# spam(0)



























































































