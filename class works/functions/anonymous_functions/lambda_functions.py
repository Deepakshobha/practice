""" square of a number """

# def squares(num):
#     return num ** 2
#
# res = squares(2)
# print(res)
# lambda args: expression

squares = lambda num: num ** 2
res = squares(2)
print(res)

""" even or not """
evens = lambda num: num % 2 == 0
# print(evens(5))

""" multiply 2 numbers """
multiples = lambda num1, num2: num1 * num2
# print(multiples(3, 6))

""" last element of the sequence """
last = lambda sequence: sequence[-1]
# print(last("hello"))
# print(last(("1", 2)))

""" palindrome or not """
palindrome = lambda string: f"{string} is a palindrome" if string == string[::-1] else "not a palindrome"
# print(palindrome("mom"))

""" even or odd """
even_odd = lambda num: f"{num} is even" if num % 2 == 0 else f"{num} is odd"
# print(even_odd(1))






















