a = [1,2,3]
t = (1,2,3)
b = 1
from sys import getsizeof
print(getsizeof(a))
print(getsizeof(t))
a.append(4)
a.append(4)
a.append(4)
a.append(4)
a.append(4)
print(a)
print(getsizeof(a))
a.append(4)
print(getsizeof(a))
a.append(4)
b = [1,2,3,4,5,6,7]
print(getsizeof(b))
b.append(8)
print(b)
print(getsizeof(b))

a = {'a':1,'b':2}
print(getsizeof(a))