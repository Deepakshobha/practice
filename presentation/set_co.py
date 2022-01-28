

# square=set()
# li = [1,2,3,4]
# for i in li:
#     square.add(i*i)
# print(square)
# #
# res={i*i for i in li}
# print(res)

#separate letters from string
string_ = "test yentra"
se = set()
for i in string_:
    se.update(i)
print(se)
res = {i for i in string_}
print(res)

#odd and even numbers  #using if condition
li = (1,2,3,4,5,6)
odd =set()
even = set()
for i in li:
    if i%2 == 0:
        even.add(i)
    else:
        odd.add(i)
print(f"odd numers:{odd} even numbers{even}")

even_= {i for i in li if i%2 == 0}
odd_ = [i for i in li if i%2 != 0]
print(even_,odd_)

#even length keep as it is odd length reverse it #using if else condition

# li = ["python",'java','selenium_','c++']
# nli = []
# for i in li:
#     if len(i)%2 == 0:
#         nli.append(i)
#     else:
#         nli.append(i[::-1])
# print(nli)
#
#
# li = [i if len(i)%2 == 0 else i[::-1] for i in li]
# print(li)

#create a tuple of state and capital in given lists
# state =['karnataka','tamilnadu']
# capital=['bangalore','chennai']
# res =[]
# for s,c in zip(state,capital):
#     res.append((s,c))
# print(res)
#
#
# res = [(s,c) for s,c in zip(state,capital)]
# print(res)

#multiple list into a single  #using 2 for loops
# li = [[1,2,3],[4,5,6],[7,8,9]]
# sli = []
#
# for i in li:
#     for j in i:
#         sli.append(j)
# print(sli)
#
# res = [j for i in li for j in i]
# print(res)



li = [1,2,3,4]
# def even_(n):
#     if n%2 == 0:
#         return f"{n} even"
#     return f"{n} odd"
# res=(map(even_,li))
# print(list(res))


evens =[ i def even_(n) if n%2 == 0]
odds = [i def even(n)if n%2 != 0]
map(evens,li)
