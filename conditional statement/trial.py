# a = 2
# # if a % 2 == 0:
# #     print(f"{a} is even")

# a = int(input("enter the value"))
# if a % 2 == 0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is not even")

# a = str(input("enter the value"))
# if a.islower():
#      print(f"{a} is lower")
# else:
#     a = a.lower()
#     print(a)

# a = "abAd"
# if a.islower():
#     print(a, "is lower")
# else:
#     print(a, "is upper")

# value = []
# if bool(value):
#     print("not a default value")
# else:
#     print("default value")

# ab = '$'
# if 'a' <= ab <= 'z':
#     print(ab.upper())
# elif 'A'<= ab <= 'Z':
#     print(ab.lower())
# else:
#     print(ab, "not a alphabet")


# ab = 'A'
# if 'a' <= ab <= 'z':
#     print(chr(ord(ab)-32))
# elif 'A'<= ab <= 'Z':
#     print(chr(ord(ab)+32))
# else:
#     print(ab, "not a alphabet")

# a = "123A"
# count = 0
# for i in a:
#     if i.isalpha():
#         i = i.lower()
#         print(i,(ord(i)-96))

a = 1234
temp = a
rev = 0
while a > 0:
    b = a % 10
    rev = rev*10 + b
    a = a//10
print(rev)
print(type(rev))


