# 1 list starts with Pp
# li = ['PHP','java','Pyton','C++']
# op = [i for i in li if i[0] in "pP"]
# print(op)

# # 2 <6 letter
# li = ['microsoft','wipro','l&t','sony','facebook']
# op = [i for i in li if len(i) < 6]
# print(op)

# # 3 odd reverse else keep as it is
# li = ['microsoft','wipro','l&t','sony','facebook']
# op = [i if len(i) % 2 != 0 else i[::-1] for i in li ]
# print(op)

# # 4 power of their indices
# li = [1,2,3,4]
# op = [li[i]**i for i in range(len(li))]
# print(op)

# 5 string and length in tuple list comprehension
# li = ['microsoft','wipro','l&t','sony','facebook']
# op = [(i,len(i)) for i in li]
# print(op)

# #6  print numeric values
# li = ['microsoft','wipro','l&t','sony','facebook',1,12,1.2,3.4]
# op = [i for i in li if isinstance(i,(int,float))]
# print(op)

# # 7 rotate the character in the list
# li = ['microsoft','wipro','l&t','sony','facebook',1,12,1.2,3.4,"25","100"]
# op = [i[::-1] for i in li if isinstance(i,(str))]
# print(op)

# 10 even number from 01 to 50
# op = [i for i in range(51) if i % 2 == 0]
# print(op)

# 9 maximum number
# li = [0,1,2,3,4,3,3,1,0,4,3]
# op = [max(li)]
# print(op)


# 8 check series continuation
# # a = [10,12,14,16,18]
# # b = [20,22,24,26,32]
# # l1 =[]
# # l2 = []
# # for i in range(len(a)-1):
# #     c = a[i] - a[i+1]
# #     l1.append(c)
# # for j in range(len(b)-1):
# #     d = b[j] - b[j+1]
# #     l2.append(d)
# # if l1 == l2:
# #     print('matching')
# # else:
# #     print('not matching')

# 2nd method
