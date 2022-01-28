""" to print bangalore 10 times """
print("bangalore\n" * 10)

""" no of digits and alphabets"""
string = "hello123hai86"
alp_count = 0
dig_count = 0

for char in string:
    if "a" <= char <= "z" or "A" <= char <= "Z":
        alp_count += 1

    elif "0" <= char <= "9":
        dig_count += 1
# print(alp_count, dig_count)

""" create a string by swapping the cases"""
s = "HeLlo WOrlD"
res = ""

for char in s:
    if "a" <= char <= "z":
        res += chr(ord(char) - 32)
    elif "A" <= char <= "Z":
        res += chr(ord(char) + 32)
    else:
        res += char
# print(res)

""" create a string with consonants """

s = "hello world"
res = ""

for char in s:
    if char.lower() not in "aeiou":
        res += char

# print(res)

""" search for a character and return its first occurrence index """

s = "hello world"
char = "o"

for item in s:
    if char == item:
        ind = s.index(char)
        # print(f"{char} is present at index {ind}")
        break

for index in range(len(s)):
    if char == s[index]:
        # print(f"{char} is present at index {index}")
        break

for index, item in enumerate(s):
    if char == item:
        # print(f"{char} is present at index {index}")
        break

""" print char and ascii value if it is a vowel"""
s = "hello"

# for char in s:
#     if char.lower() in "aeiou":
#         print(char, ord(char))

""" print word and its length"""
s = "hello world"
words = s.split()

# for word in words:
#     print(word, len(word))

""" print words starting with vowels """
sentence = " hai everyone, welcome to the python class"

words = sentence.split()

# for word in words:
#     if word[0].lower() in "aeiou":
#         print(word)

""" count the characters without any inbuilt functions """
s = "hello world"
count = 0

for char in s:
    count += 1

# print(count)

""" reversing a string """
string = "hello"

# reversed()

for char in reversed(string):
    print(char, end="")
print()
# range()
for index in range(len(string)-1, -1, -1):
    print(string[index], end="")
print()
# using concatenation

res1 = ""

for char in string:
    res1 = char + res1
print(res1)