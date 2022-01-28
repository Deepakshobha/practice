'''li = ['python', 'java', 3, 4]
for index, item in enumerate(li):
    print(index,item)'''

'''li = ['python', 'java', 3, 4]
for i in range(len(li)-1,0,-1):
    print(li[i])'''

'''li = ['python', 'java', 3, 4]
for i in li[::-1]:
    print(i)'''

'''li = ['python', 'java', 3, 4]
for i in reversed(li):
    print(i, end = ' ')'''

''''li =['python', 'java', 3, 4]
for i in range(0, len(li), 2):
    print(li[i], end = ' ')'''


'''li = ['python', 'java', 3, 4]
for i in range(len(li)):
    if i%2 != 0:
        print(li[i])'''

'''li = ['python', 'java', 3, 4, 5.2]
for i in li:
    if isinstance(i, (int, float, bool, complex)):
        print(i)'''

'''li = ['python', 'java', 'selium']
for i in li:
    b = len(i)
    print((i,b))'''
''''li = ['python', 'java', 'selium', 'abc', 'abcde']
l = []
for i in li:
    if len(i) % 2 == 0:
        l.append(i)
print(l)'''

'''li = ['python', 'java', 'selium', 'abc', 'abcde',1, 1.2, 3]
l = []
for i in li:
    if isinstance(i, str):
        l.append(i[::-1])
    else:
        l.append(i)
print(l)'''
'''file = ['youtube.com', 'amazon.pdf', 'apple.xls']
for i in file:
    a = i.split(".")
    if len(a[0]) % 2 == 0:
        print(a)
        pass
    else:
        print(a[0])'''
'''a = [1, 2, 3, 4, 3]
b = 5
for index, item in enumerate(a):
    if item == b:
        print(index)
        break
else:
    print('element not present')'''
'''a = [1,22,3,48,5,68,55]
for n in a:
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            print(n)

a = ['python', 'mom', 'dad']
for i in a:
    if i == i[::-1]:
        print(i)'''
'''a = ['python', 'mom', 'dad']
b = set()
for i in a:
    if i == i[::-1]:
        (b.update([i]))
print(b)

a = {1,2,3,4,5}
b = 5
for i in a:
    if i == b:
        a.discard(b)
        break
print(i)'''

s1 = "hai"
s2 = "hey"
for item1, item2 in (zip(s1,s2)):
    print(item1,item2)












