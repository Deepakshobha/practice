# l = [1,9,3,6,8]
# print(sorted(l))
#
# l = (1,9,3,6,8)
# print(sorted(l))
#
# l = ['python','c','b','jav']
# print(sorted(l))
#
# l = {'python','c','b','jav'}
# print(sorted(l))
#
#
# l = {'python':1,'c':6,'b':5,'jav':3}
# print(sorted(l))
#
# l = {'python':1,'c':6,'b':5,'jav':3}
# print(sorted(l.items()))


# l = [1,9,3,6,8]
# print(sorted(l, reverse=True))

# based on length
# l = ['python','c','b','jav']
# print(sorted(l,key=len))


# find  long and short keyword
# s = 'python is a programming language'
# r = s.split()
# long = []
# short = []
# b=(sorted(r,key=len))
# short = [b[0]]
# long = [b[-1]]
# print(long,short)

# s = 'python is a programming language'
# r = s.split()
# short,*rest,longest = sorted(r,key=len)
# print((longest,(len(longest))),(short,(len(short))))
#
# # last element in list
# s = 'python is a programming language'
# r = s.split()
# print(sorted(r,key=lambda item:item[-1]))

# middle character
# s = ['hai','javaf','pythont','rubyg','programt']
# print(sorted(s,key=lambda item:len(item)//2))


# d = {"gmail":5,"apple":3,'walmart':1,'bat':7}
# # print(sorted(d))
# # print(sorted(d.keys()))
# print(sorted(d.values()))
# print(sorted(d.items()))
# print(sorted(d,key=len))
# print(sorted(d.keys(),key=len))
# print(sorted(d.items(),key=lambda item:len(item[0])))
# print(dict(sorted(d.items(),key=lambda item:len(item[0]))))


# based on keys last item
# d = {"gmail":5,"apple":3,'walmart':1,'fish':7}
# print(dict(sorted(d.items(),key=lambda item:(item[0][-1]))))

# based on values
# d = {"gmail":5,"apple":3,'walmart':1,'fish':7}
# print(dict(sorted(d.items(),key=lambda item:item[-1])))
# print(sorted(d,key=lambda item:d[item]))

# temperature=[('d',32),('m',27),('k',30),('c',35)]
# print(sorted(temperature, key=lambda item:item[-1]))


# most repeated word
# sentence = "hi hello how are you how is your lengh"
# d = {}
# r = sentence.split()
# for i in r:
#     if i not in d:
#         d[i] = r.count(i)
#     else:
#         d[i] = r.count(i)
# res=(sorted(d.items(), key=lambda item:item[-1]))
# print(res[-1])

# sentence = "hi hello how are you how is your lengh"
# r = sentence.split()
# d = {item:r.count(item) for item in r}



# longest word
# sentence = "hi hello how are you how is your lengh"
# r = sentence.split()
# op = {i:len(i) for i in r}
# res = (sorted(op.items(), key = lambda item:item[-1]))
# print(res[-1])

# sort based on names
# l = [{'name':'ram','class':3,'age':12},{'name':'shyam','class':15,'age':16},{'name':'bheem','class':5,'age':52}]
# print(sorted(l,key = lambda item:item['name']))
# print(sorted(l,key = lambda item:item['class']))
# print(sorted(l,key = lambda item:item['age']))


import os
print(os.getcwd())
path = r"C:\Users\Deepak M\Desktop\pythonProject2\practice\directory\sample"
with open(path):as file1





