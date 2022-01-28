
# word and count pair
s = "hail hello how hello how"
r = s.split()
op = {i:r.count(i) for i in r}
# print(op)

# word and count pair even length
s = "hail hello how hello how python is program"
r = s.split()
op = {i:len(i) for i in r if len(i) % 2 == 0}
# print(op)

