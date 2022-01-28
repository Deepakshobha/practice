# a = ["hai",1,2,4,6,"hello"]
#
# # to fetch o
# print(a[5][-1])
#
# a = [1,2,3,[4,5,6,"hai"],4]
# print(a[3][3][2])
#
# a = [1,2,3,[4,5,6,["hai"],6],4]
# print(a[3][3][0][2])
#
# a = [[[1,2,3,[4,5,6,["hai"],6],4]]]
# print(a[0][0][3][3][0][2])
#
# a = ['hai','hello']
# b = [1,2,3]
# print(a+b)
#
# print("hello world".title())
# print("hello world".find('l',3,6))
#
#
# print("hai hello welcome to python".startswith("hai",5,10))
#
#
#
# a = {'1','2'}
# a = ('1','2')
# a ={'a':1,"b":2}
# print('-'.join(a))
#
#
# a ="this is my string"
# print(a.split())
# print(a.split('s'))
# print(a.split('s',1))
# print(a.rsplit(" ",5))

# li =[1,2,3]
# li.extend([4,5])
# print(li)
#
# li = [1,2,3,5]
# li.insert(1,"hai")
# print(li)
#
#
# li = [1,2,3,4,5,"hai"]
# print(li.pop())
# print(li.pop(-1))
# print(li)
# print(li.pop(-5))


# names = ["apple","universe",'world','ball']
# names.sort()
# print(names)
# names.sort(reverse=True)
# print(names)
# names.sort(reverse=True,key=len)
# print(names)
# names.sort(reverse=True,key=)
# print(names)

# a =[[[1,2,3]]]
# print(a[0][0][2])
# a = [[[[1,2,3],[4,5,6],"test"],"yentra"],[[7,8,9]]]
# print(a[1][0][2])
#
# print(a)

# from copy import copy
# a = [1,2,3,[10,30]]
# b = copy(a)
# print(a)
# print(b)
# a.append([2,3])
# print(a)
# print(b)
# a[3][1] = "a"
# print(a)
# print(b)



# A = [1,2,3]
# B =[1,2,3]
# t = ()
# typ


# a = {1,2,3,4}
# b = {3,4,5,6}
# c = {3,1,7}
# print(a.symmetric_difference(b))
# print(a.clear())
# print(a)
# print(b.discard(8))
# print(b)

# x ={'a', 'b', 'c'}
# y = {'f','a','e','b', 'c'}
# print(x.issubset(y))
# print(x.issuperset(y))
# print(y.issuperset(x))
# print(set("hai"))

# a = {1,2,3,4}
# b = {3,4,5,6}
# c ={5,6,7,8}
# d = {5,6,7,9}
# print(a.union(b,c,d))
# d = {'abc':30,"efg":65}
# print(d)
#
# d ={'Bangalore':20, 'chennai':30, 'Delhi':40}
# print(d['Bangalore'])
# print(d['Delhi'])
# print(d.get('Bangalore'))
# print(d.get('delhi',25))
# print(d)
# print(d.get("mumbai"))
# print(d.get("mumbai","key not found"))
# print(d)


# d ={'Bangalore':20, 'chennai':30, 'Delhi':40}
# print(d.items())
# print(d.keys())
# print(d.values())
# print(d.popitem())
# print(d)
# print(d.pop('Bangalore'))


# d ={'Bangalore':20, 'chennai':30, 'Delhi':40}
# d['mysore'] = 20
# print(d)
# d.update({'mysore':26.5,'mumbai':40})
# print(d)
# d.update(mumbai=45)
# print(d)

# l = ['apple', 'ball', 'cat']
# d.fromkeys(l)

d1 ={'Bangalore':20, 'chennai':30, 'Delhi':40}
d2 = {"mysore":30,"mangalore":60}
print({**d1,**d2})
print(d1|d2)