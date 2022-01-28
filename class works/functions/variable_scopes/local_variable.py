# accessing a local variable inside a function
def spam():
    a = 10
    print(a)


# spam()
# print(a)    # NameError


# def spam():
#     global a
#     a = 10
#     print(a)
#
#
# spam()
# print(a)


def f1():
    x = 10
    def f2():
        nonlocal x
        x += 2
        print(x)
    f2()
f1()








