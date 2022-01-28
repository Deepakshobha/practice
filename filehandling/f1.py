import csv
import os
from collections import Counter
from itertools import islice
path=r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\csv_files\sample.csv"
# 1 count the lines
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(count, line)

# 2 number of words
# with open(path) as file:
#     count = 0
#     for line in file:
#         r = line.split()
#         for word in r:
#             count += 1
#     print(count)
#
# # 3 lines from last line
# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)
#
# # 4 count spaces
# with open(path) as file:
#     count = 0
#     for line in file:
#         for j in line:
#             if j in ' ':
#                 count += 1
#     print(count)

# with open(path) as file:
#     count = 0
#     for line in file:
#         spaces = line.count(' ')
#         count += spaces
#     print(count)

# 5 starting with vowels
# with open(path) as file:
#     count = 0
#     for line in file:
#         for word in line.split():
#             if word[0] in "aeiouAEIOU":
#                 count += 1
#     print(count)

# 6 word and count pair in dictionary
# d = {}
# with open(path) as file:
#     for line in file:
#         r = line.split()
#         for word in r:
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
#     print(d)

# from collections import defaultdict
# d=defaultdict(int)
# with open(path) as file:
#     for line in file:
#         r = line.split()
#         for word in r:
#             d[word] += 1
#     print(d)
# 7 print only ip ipaddress
# path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\access-log.txt"
# l=[]
# with open(path) as file1:
#     for i in file1:
#         l.append(i.split()[0])
#     print(l)

# path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\access-log.txt"
# l=[]
# with open(path) as file1:
#     for i in file1:
#         r = i.split()
#         l.append(r[0])
#     print(l)

# path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\access-log.txt"
# l=[]
# with open(path) as file1:
#     for line in file1:
#         if line.strip():
#             r = line.split()
#             l.append(r[0])
#     print(l)

# 9 dictof ip addresss and count pair
# path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\access-log.txt"
# l=[]
# d = {}
# with open(path) as file1:
#     for line in file1:
#         if line.strip():
#             r = line.split()
#             l.append(r[0])
#     for j in l:
#         if j not in d:
#             d[j] = 1
#         else:
#             d[j] += 1
#     print(d)


# path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\access-log.txt"
# l=[]
# d = {}
# with open(path) as file1:
#     for line in file1:
#         if line.strip():
#             r = line.split()
#             if r[0] not in d:
#                 d[r[0]] = 1
#             else:
#                 d[r[0]] += 1
#     print(d)


# path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\access-log.txt"
# l=[]
# d = {}
# with open(path) as file1:
#     for line in file1:
#         if line.strip():
#             r = line.split()
#             l.append(r[0])
# ip=Counter(l)
# print(ip.most_common(1))

# print nth line number line
path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\access-log.txt"
# n = int(input('enter the value'))
# with open(path) as file1:
#     for lineno, line in enumerate(file1):
#         if lineno == n:
#             print(line)

# n = int(input('enter the value'))
# with open(path) as file1:
#     for lineno, line in enumerate(file1,start=1):
#         if lineno == n:
#             print(line)

# # wap first nth line
# n = int(input('enter the value'))
# with open(path) as file1:
#     for lineno, line in enumerate(file1,start=1):
#         if lineno <= n:
#             print(line)


# n = int(input('enter the value'))
# with open(path) as file1:
#     res = islice(file1,n)
#     print(list(res))
path = r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.txt"

# wap last nth line
# n = 2
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     file.seek(0)
#     res = islice(file,count-n,count)
#     print(list(res))
#
# # deque
# from collections import deque
# n = 2
# with open(path) as file:
#     lines = deque(file,n)
#     print(list(lines))

# path = r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.txt"
# f_path = r"C:\Users\Deepak M\Desktop\pythonProject2\practice\filehandling\f2.py"
# with open(path,'r') as file_read:
#     with open(f_path, 'w') as file_write:
#         for line in file_read:
#             file_write.write(line)


# finding the length of each line
# path = r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.txt"
# with open(path) as file:
#   for line in file:
#       print(line,len(line))
#

# # extracting message from sample.log
# path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.log"
# with open(path) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             r = line.split()
#             l.append(r[-1])
#     print(l)
# #
# counting INFO,WARN,TRACE in sample.log
# path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.log"
# with open(path) as file:
#     l = []
#     INFo = 0
#     WARN = 0
#     TRACE = 0
#     for line in file:
#         if line.strip():
#             r = line.split()
#             l.append(r[2])
#     print(l)
#     for i in l:
#         if i in 'INFO':
#             INFo += 1
#         elif i in 'TRACE':
#             TRACE += 1
#         elif i in 'WARN':
#             WARN += 1
#     print(INFo,WARN,TRACE)

# countries from footbal text
# # path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\football.txt"
# # with open(path) as file:
# #     for line in file:
# #         if line.strip():
# #             countries= line.split()
# #         print(countries[1])

# least and most occurance word
# from collections import defaultdict, Counter
# path =r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.txt"
# d = defaultdict(int)
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             r = line.split()
#             for word in r:
#                 d[word] += 1
#     c = Counter(d)
#     most, *rest, least = c.most_common()
#     print(most,least)

# import csv
# print(os.getcwd())
# with open('example.csv','w') as csv_:
#     write_obj=csv.writer(csv_)
#     write_obj.writerow(['x','y','z'])
#     write_obj.writerow([1, 2, 3])
# from collections import defaultdict
# path = r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\csv_files\vaccination_data.csv"
# with open(path) as file:
#     r_obj = csv.DictReader(file)
#     header = next(r_obj)
#     for row in r_obj:
#         d = defaultdict(list)
#         d[row['DATE_UPDATED']] += [(row['COUNTRY'],row['TOTAL_VACCINATIONS'])]
# res  = sorted(d.items())
# print(res[-1])



from itertools import islice
# def asd(start,end):
#     with open(r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.txt", 'r') as f1:
#         s = islice(f1,start,end+1)
#         for line in s:
#             print(line)
# asd(0,3)

# from itertools import islice
# def asd(start):
#     with open(r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.txt", 'r') as f1:
#         # s = islice(f1,start,end+1)
#         count = 0
#         for line in f1:
#             count += 1
#         f1.seek(0)
#         s = islice(f1,count-start)
#         for i in s:
#             print(i)


# asd(5)
# from collections import deque
# def asd(start):
#     with open(r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\txt_log_files\sample.txt", 'r') as f1:
#         d =deque(f1,start)
#         for line in d:
#             print(line)
# asd(5)



# def asd(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args,**kwargs)
#         return abs(result)
#     return wrapper
# @asd
# def sub(a,b):
#     print(a-b)
#
# sub(-1,2)



class Simple():
    def __init__(self,item):
        self.item = item

    def __iter__(self):
        return iter(self.item)

s = Simple([1,2,3,4])
for item in s:
    print(item)