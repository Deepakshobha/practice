# wap index and corresponding element
# l = ['python',10, 3.2, 'selenium_', 'java']
# op = [item for item in enumerate(l)]
# print(op)

# l = ['python',10, 3.2, 'selenium_', 'java']
# op = [(item,l[item]) for item in range(len(l))]
# print(op)

# wap list reverse order
# l = ['python',10, 3.2, 'selenium_', 'java']
# op = [item for item in l[::-1]]
# print(op)

# l = ['python',10, 3.2, 'selenium_', 'java']
# op = [l[item] for item in range(len(l)-1,-1,-1)]
# print(op)

# l = ['python',10, 3.2, 'selenium_', 'java']
# op = [item for item in reversed(l)]
# print(op)

# alternate number
# li = list(range(10))
# odd = [item for item in li if item % 2 != 0]
# even = [item for item in li if item % 2 == 0]
# print(odd, even)

# li = [1,2,3,4,5]
# op = [li[i] for i in range(0,len(li),2)]
# print(op)


# odd and even
# li = list(range(10))
# odd = [item for item in li if item % 2 != 0]
# even = [item for item in li if item % 2 == 0]
# print(odd, even)

# alternate even and odd length element in list
# li = ['python','selenium_', 'java','abc']
# odd = [item for item in li if len(item) % 2 != 0]
# even = [item for item in li if len(item) % 2 == 0]
# print(odd,even)

# print only integer in list
# li = ['python','selenium_', 'java','abc',1,12,13,14]
# op = [i for i in li if isinstance(i,int)]
# print(op)

# print only single value data type
# li = ['python','selenium_', 'java','abc',1,12,13,14,True,1.2,3+4j]
# op = [i for i in li if isinstance(i,(int,float,bool,complex))]
# print(op)

# lengh of each string in list
# li = ['python','selenium_', 'java','abc']
# op = [(i,len(i)) for i in li]
# print(op)

# even lengh save as it is odd lengh reverse and store
# li = ['python', 'java', 'selium', 'abc', 'abcde']
# l = []
# for i in li:
#     if len(i) % 2 == 0:
#         l.append(i)
#     else:
#         l.append(i[::-1])
# print(l)
#
# li = ['python', 'java', 'selium', 'abc', 'abcde']
# res = [item if len(item) % 2 == 0 else item[::-1] for item in li]
# print(res)

# li = ['amazon', 'walmart', 'email']
# output = [item for item in li if item[0] in "aeiouAEIOU"]
# print(output)

#reverse if its string else keep as it is
# li = ['amazon', 'walmart', 'email',3,1.2]
# output = [i[::-1] if isinstance(i,str) else i for i in li]
# print(output)

#print only extension
li = ['amazon.com', 'walmart.in', 'email.com']
op = [(a[1]),a = item.split('.') for item in a ]
print(op)