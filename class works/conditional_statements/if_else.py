""""""
""" WAP to check if the given input number is even or odd"""
# number = 3
#
# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")

""" WAP to check if the character is lowercase or uppercase"""

# char = "r"
#
# if "a" <= char <= "z":
#     print(f"{char} is lowercase")
#
# else:
#     if "A" <= char <= "Z":
#         print(f"{char} is uppercase")
#     else:
#         print(f"{char} is not an alphabet")

#####################################################

# char = "r"
# if "a" <= char <= "z":
#     print(f"{char} is lowercase")
#
# elif "A" <= char <= "Z":
#     print(f"{char} is uppercase")
#
# else:
#     print(f"{char} is not an alphabet")

""" WAP to check if the given iterable is empty or not """

iterable = "hai"

# if len(iterable) > 0:
#     print("the iterable is not empty")
#
# else:
#     print("iterable is empty")
#
# if bool(iterable):
#     print("Iterable is not empty")
# else:
#     print("Iterable is empty")

# if iterable:
#     print("not empty")
# else:
#     print("empty")

""" WAP to check if the given value is default or non default value"""

# value = []
#
# if value:
#     print("It is non default value")
# else:
#     print("default value")


#############################################################
""" WAP to convert lowercase to uppercase and vice-versa """

# char = "N"
#
# if char.islower():
#     upper_char = char.upper()
#     print(upper_char)
#
# elif char.isupper():
#     lower_char = char.lower()
#     print(lower_char)
#
# else:
#     print("character is not an alphabet")

# char = "n"
#
# if "a" <= char <= "z":
#     print(chr(ord(char) - 32))
#
# elif "A" <= char <= "Z":
#     print(chr(ord(char) + 32))
#
# else:
#     print("character is not an alphabet")

################################################################
# string = "MOm"
# a = string.lower()
#
# if a == a[::-1]:
#     print(f"{string} is a palindrome")
# else:
#     print(f"{string} is not a palindrome")

##############################################################
# number = 1231
# str_num = str(number)
#
# if str_num == str_num[::-1]:
#     print(f"{number} is a palindrome")
# else:
#     print(f"{number} is not a palindrome")

###############################################################
""" WAP to check if the iterable has even number of elements """
# list_ = [10, 20, 30, 40]
#
# if len(list_) % 2 == 0:
#     print("iterable has even numbered elements")
# else:
#     print("iterable has odd numbered elements")

###############################################################
""" WAP to check if the first digit in the given number is even or odd """
number = 1234
str_num = str(number)

# if int(str_num[0]) % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# print("number is even" if int(str_num[0]) % 2 == 0 else "number is odd")

############################################################################

# char = "a"
# d = {}
# if char.lower() in "aeiou":
#     # d[char] = ord(char)
#     # d.update({char: ord(char)})
#     # d.setdefault(char, ord(char))
#     print({char: ord(char)})
#
# print(d)

#check given chr is upper convert to lower case lower to upper

ab = 'n'
if 'A'<=ab<='Z':
    print(chr(ord(ab)+32))
else:
    print(chr(ord(ab) - 32))



#wap to check weather given value is divisible by  5 or not if divisible by 5 take it store inside the dictionary as a key and value is cube of that
#else key and square of that value
#
# a = 2
# d = {}
# if a%5 == 0:
#     d[a] = a**3
#     print(d)
# else:
#     d[a] = a**2
#     print(d)
#
# a = 2
# if a%5 == 0:
#     print({a:a**3})
# else:
#     print({a:a**2})


#user id password or matching or not
d = {'user id':'shobha','password':12345}
userid = 'shobha'
password = 12345
if d['user id'] == userid and d['password'] == password:
    print('valid')
else:
    print('invalid')





























































