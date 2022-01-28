# for i in range(1, 11):
#     print(i)

def count_10(start, end):
    for i in range(start, end+1):
        print(i, end=" ")

# count_10(1, 10)


def count_(n):
    if n <= 10:
        print(n)
        n += 1
        count_(n)
    else:
        return

# count_(1)


def count_(start, end):
    if start > end:
        return
    print(start)
    count_(start+1, end)

# count_(1, 10)


""" 10 to 1 """

def count_down(start, end):
    if start < end:
        return
    print(start)
    count_down(start-1, end)

# count_down(10, 1)

""" add digits of the number """

# using loop

n = 123
sum = 0

while n > 0:
    last = n % 10
    sum += last
    n = n // 10

# print(sum)

# recursion

def sum_(num, sum=0):
    if num > 0:
        last = num % 10
        sum += last
        num = num // 10
        return sum_(num, sum)
    else:
        return sum

# print(sum_(123))


""" sum of first n numbers """

def sum_n(n, sum=0):   # 4
    if n > 0:
        sum += n
        return sum_n(n-1, sum)
    return sum

# print(sum_n(4))

""" factorial of a number """


def fact_(n, fact=1):   # 4
    if n > 0:
        fact *= n
        return fact_(n-1, fact)
    return fact


# print(fact_(5))

""" count number of digits in a number """

def count_digits(num, count=0):
    if num > 0:
        count += 1
        return count_digits(num//10, count)
    return count

# print(count_digits(123))

""" reverse a string """


def reverse_string(string, i=0, res=""):
    if i < len(string):
        res = string[i] + res
        return reverse_string(string, i+1, res)
    return res


# print(reverse_string("hai"))

























































