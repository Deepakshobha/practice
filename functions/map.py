# li = ['ab','bc']
# def func(string):
#     return [string]
#
# res = (map(func,li))
# print(list(res))


# li = [1,2,3,4,5]
# def func(num):
#     return num**num
# res = map(func,li)
# print(list(res))

li = [1,2,3,4,5]
def func(item):
    if item[0] % 2 == 0:
        return item[1]*item[1]
res = list(map(func,enumerate(li)))

def abc(res):
    return res

print(list(filter(abc,res)))

