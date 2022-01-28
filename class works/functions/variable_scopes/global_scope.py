# a = 10

# accessing a global variable inside a function
# def spam():
#     print(a)

# spam()

# modify global variable
def spam():
    a = 5
    global a
    print(a)

spam()
print(a)



