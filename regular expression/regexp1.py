import re
# # greeting = "Hello world welcome to regular expression in python hello world hello n."
# # print(greeting)
# # print(re.findall("hello",greeting))
# # print(re.findall("hello",greeting,re.IGNORECASE))
# # print(re.findall("h",greeting,re.IGNORECASE))
# # print(re.findall("he",greeting,re.IGNORECASE))
# # print(re.findall(r".",greeting)) #dot matches with any character except newline
# # print(re.findall(r"h.",greeting)) #character dot---any character #h followed by any character one character #after h one character must be there
# # print(re.findall(r"a.b","acb"))
# # print(re.findall(r"a.b","a b"))
# # # print(re.findall(r"a.b","a2b"))
# # print(re.findall(r"a.b","ab"))   #empty list expecting after a one character
# # print(re.findall(r"a.b","a2b a*b"))
# # print(re.findall(r"a.b","abcde"))
# # print(re.findall(r"^hello","hello world hello world")) #^ specify the start of string # hello should be begining of the string
# # print(re.findall(r"^hello","world hello"))
# # print(re.findall(r"hello$","world hello")) # $ pattern should at the end of the string
# # print(re.findall(r"a.a","ana"))
# # print(re.findall(r"a.a","ana hello worls axa"))
# # print(re.findall(r"a..a","ana"))
# # print(re.findall(r"a..a","anna"))
# # print(re.findall(r"a..a","a__a"))
# # print(re.findall(r"a.*a","a__--a")) # * will match ocuurence of pre-character 0 or any number of accurence
# # print(re.findall(r"an*a","aa"))
# print(re.findall(r"am*a","ama"))
# print(re.findall(r"am*a","aa"))
# print(re.findall(r"a.*a","hello world ana"))
# print(re.findall(r"a.*a$","hello world ana"))
# print(re.findall(r"^a.*a","hello world ana"))
# print(re.findall(r"^hello$","hello world ana"))
# print(re.findall(r"^hello$","hello"))
# print(re.findall(r"^hello$","hello is hello"))
# print(re.findall(r"an*a","ana"))
# print(re.findall(r"an*a","ana"))
# print(re.findall(r"an*a","annnnma"))
# print(re.findall(r"an+a","ana")) # + will match ocuurence of pre-character 1 or any number of accurence
# print(re.findall(r"an+a","annnna"))
# print(re.findall(r"an+a","aa"))
# print(re.findall(r"an?a","annnna")) # ? 0  or 1 ocuurence
# print(re.findall(r"an?a","ana"))
# print(re.findall(r"an?a","aa"))
# print(re.findall(r"color","what color do you like"))
# print(re.findall(r"colou?r","what color do you like"))
# # print(re.findall(r"colou?r","what colour do you like"))
# # print(re.findall(r"https?://","https://www.google.com"))
# # print(re.findall(r"https?://","http://www.google.com"))
# print(re.findall(r"[aeiou]","hello world welcome to python")) #[] character set in python # matches each character
# print(re.findall(r"[hello]","hello world"))
# print(re.findall(r"[0123456789]", "the cost of this book is $100"))
print(re.findall(r"[0-9]", "the cost of this book is $100")) # - represents range
# print(re.findall(r"[0-5]", "the cost of this book is $92500"))
# # print(re.findall(r"[a-z]", "the cost of this book is $100"))
# # print(re.findall(r"[A-Z]", "the cost of this book is $100 a A b Z"))
# print(re.findall(r"[0-9]+", "the cost of this book is $100")) #[]+ concatenation #keeps matching as long as there is a match
# print(re.findall(r"[0-9]+", "the cost of this book is $100 go to 250"))
# # print(re.findall(r"[A-Z]+", "the cost of this book is $100 a A b Z"))
# # print(re.findall(r"[a-z]+", "the cost of this book is $100"))
# print(re.findall(r"\d", "the cost of this book is $100 go to 250")) # \d numbers[0-9]
# print(re.findall(r"\d+", "the cost of this book is $100 go to 250"))
# # print(re.findall(r"\d+", "the cost of this book is $100 go to 250"))
# # print(re.findall(r"[^0-9]", "the cost of this book is $100")) # ^ inside the character set signifies negation except number prints everything
# print(re.findall(r"[^0-9]+", "the cost of this book is $100"))
# print(re.findall(r"[^\d+]+", "the cost of this book is $100 go to 250"))
# print(re.findall(r"[^A-Z]", "the cost of this book is $100 a A b Z"))
# print(re.findall(r"[^A-Z]+", "the cost of this book is $100 a A b Z"))
# print(re.findall(r"[a-zA-Z]", "the cost of this book is $100 a A b Z"))
# # print(re.findall(r"[a-zA-Z0-9]", "the cost of this book is $100 a A b Z"))
# # print(re.findall(r"[a-zA-Z0-9]+", "the cost of this book is $100 a A b Z"))
# # print(re.findall(r"[^a-zA-Z0-9]+", "the cost of this book is $100 a A b Z"))
# print(re.findall(r"[\D]", "the cost of this book is $100 a A b Z")) #D represents negatation of numbers
# print(re.findall(r"[\w]+", "the cost of this book is $100 a A b Z")) #alphanumric value and underscore
# print(re.findall(r"[\W]+", "the cost of this book is $100 a A b _Z"))
# # print(re.findall(r"\s", "the cost of this book is $100")) #\s matches white spaces
# # print((re.findall(r"\S", "the cost of this book is $100 a A b Z"))) #S apart from white spaces
#
#
# from requests import request
# def abc():
#     response = request("GET",r"http://demowebshop.tricentis.com/desktops")
#     links = response.text
#     result = re.findall("\s*<a\s",links)
#     print(len(result))
#
# abc()



result = re.findall(r'\bcat\b', 'cat indicat pcat')
print(result)