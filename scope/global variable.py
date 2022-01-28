a = 10
def func():
    global a
    a += 1
    return a
print(func())