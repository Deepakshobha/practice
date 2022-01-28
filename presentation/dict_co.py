#dict comprhension using list
li = [1,2,3,4]
res = {i:i**i for i in li}
print(res)

#word and count pair
sentence="hello world how are you"
r =sentence.split()
res = {i:len(i)for i in r}
print(res)

#word and count pair of even length
# sentence="hello world how are you python is a simple language"
# r =sentence.split()
# res = {i:len(i) for i in r if len(i)%2 == 0}
# print(res)

#odd length reverse it else keep as it is
# sentence="hello world how are you python is a simple language"
# r =sentence.split()
# res = {i:i if len(i)%2 == 0 else i[::-1]for i in r }
# print(res)

# #flip key and value in dictionary
# d = {'hello': 5, 'world': 5, 'how': 3, 'are': 3, 'you': 3}
# res = {value:key for key,value in d.items()}
# print(res)
#
# #using 2 if
# d = {'apple':38,"ball":44,"cat":33}
# res = {k:v for k,v in d.items() if v%2 == 0 if v<40}
# print(res)




def sample(a,b):
    a=10
    b=20
    c=a+b
    return c
print(sample(10,20))
