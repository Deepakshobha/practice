import re
# sentence = "hello hi world hello howo are you"
# r =sentence.split()
# for i in r:
#     if i[0] in 'h': # i[0] == 'h
#         print(i)
#
# print(re.findall(r"\bh\w+",sentence))
# # print(re.findall(r"\bh.*\b",sentence))
# print(re.findall(r"\bh\w*\b",sentence))
#
# print(re.findall(r"\b\w+o\b",sentence))
# print(re.findall(r"\w+o\b",sentence))

# word = "SOny12India Pvt34 ltd567 bangalore "
# l = (re.findall(r"\d",word))
# sum = 0
# for item in l:
#     sum += int(item)
#
# print(sum)$
#
# l = (re.findall(r"\d+",word))
# print(l)
# for item in l:
#     sum += int(item)
#
# print(sum)

#spaces
# print(len(re.findall(r"\s",word)))


# sentences = "hai hello how ar@e you $123 welcome!!! && @@ he"
# letters = (re.findall(r"\w",sentences))
#
# count = {c:letters.count(c) for c in letters}
# print(count)

# filter digits'
# sentences = "hai hello how ar@e you $ 12356 welcome!!! && @@ he"
# l=(re.findall(r"\D",sentences))
# s= ' '.join(l)
# print(s)

#ignorespecial character
# sentences = "hai hello how ar@e you $ 12356 welcome!!! && @@ he"
# l=(re.findall(r"\w+",sentences))
# for i in l:
#     print ((i,len(i)))
# c = {i:len(i) for i in l}
# print(c)

# upper and lower
# sentences = "hai hello how BNFT JKK ar@e you $ 12356 welcome!!! && @@ he"
# up=len(re.findall(r"[A-Z]",sentences))
# lower=len(re.findall(r"[a-z]",sentences))
# print(up,lower)

#extract extensions
# dmsg = """hashaK gmail.com jkjdsk
#        fjdfdsklfjdsl archive.zip bsbjs"""
# print(re.findall(r"\.[a-zA-Z]",dmsg)) #\. checks for .
# print(re.findall(r"\.[a-zA-Z]+",dmsg))


# file = """Graphic User
#           Comma Separated Values"""
#
# for item in file:
#


# numbers = ['456-123-4567','123-586-3698','5556-58-666','800-123-9863','900-235-6987']
# for item in numbers:
#     match = re.findall(r"\d{3}-\d{3}-\d{4}",item)
#     if match:
#         print(match)
#     else:
#         print(f"item {item} invaild")

# start with 800 and 900
# numbers = ['456-123-4567','123-586-3698','5556-58-666','800-123-9863','900-235-6987']
# for item in numbers:
#     match = re.findall(r"[89]00",item)
#     if match:
#         print(match)
#     else:
#         print(f"item {item} invaild")

#word starts with vowel character
# sentences = "hai hello how BNFT JKK ar@e you $ 12356 is welcome!!! && @@ he"
# print(re.findall(r"\b[aeiou]\w+",sentences))
# print(re.findall(r"\b[aeiou]\w+",sentences))
# print(re.findall(r"\b[^aeiou\s]\w+",sentences))

sentences = "hai hello how BNFT JKK ar@e you $ 12356 is welcome!!! && @@ he"
print(re.findall(r"\b\w{3}\b",sentences))