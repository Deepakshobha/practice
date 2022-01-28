import re
sentence = "the pincode of bangalore is 560001 and the telephone code is 080 ph:1234567890"
print(re.findall(r"\d+",sentence))
print(re.findall(r"\d\d\d\d\d\d",sentence))
print(re.findall(r"\d{6}",sentence))
# \b word boundry = transision b/w non word character to word character and vice versa
print(re.findall(r"\b\d{6}\b",sentence))

word = "I am Travelling from BLR and DHL on 26-JUL-2022"
print(re.findall(r"[A-Z]{3}",word))
print(re.findall(r"\b[A-Z]{3}\b",word))
words = "I am Travelling from BLR and DHL on 26JUL2022"
print(re.findall(r"\b[A-Z]{3}\b",words))

print(re.findall(r"\w{2}","hi hello and python is programming"))
print(re.findall(r"\w{2,5}","hi hello"))
print(re.findall(r"\b\w{2,5}\b","hi hello and python is programming")) #minimum 2 letter max 5 letter
print(re.findall(r"w{2,}","hi hello and python is programming"))