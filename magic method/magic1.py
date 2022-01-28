import csv
# path = r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\csv_files\employees.csv"
# def read_csv():
#     with open(path) as f:
#         rows = csv.DictReader(f)
#         header = next(rows)
#         records  =[]
#         for row in rows:
#             records.append(row)
#         return records
#
# data = (read_csv())
#
# #calculate total pay of all the employees
# def total_salary(data):
#     total = 0.0
#     for item in data:
#         total = total + float(item['pay'])
#     return total
#
# print(total_salary(data))


#male female

# def gender(data):
#     from collections import defaultdict
#     gen =defaultdict(int)
#     for item in data:
#         g = item['gender']
#         gen[g] += 1
#     return gen
# print(gender(data))

#sort based names
# by_name = sorted(data, key=lambda item:item['name'])
#
# for item in by_name:
#     print(item)
#
# for item in reversed(by_name):
#     print(item)
#
# #unique teams
# teams = set([item['team'] for item in data])
# print((teams))
# teams = {item['team'] for item in data}
# print((teams))

#salry > 5000
# for item in data:
#     if float(item['pay']) > 75000:
#         print(item)


import csv
path = r"C:\Users\Deepak M\Desktop\pythonProject2\practice\files_directory\csv_files\vaccination_data.csv"
def read_csv():
    with open(path) as f:
        rows = csv.DictReader(f)
        header = next(rows)
        records  =[]
        for row in rows:
            temp = {"country":row['COUNTRY'],"date":row['DATA_SOURCE'], "cases":row['TOTAL_VACCINATIONS']}
            records.append(temp)
        return records

data = (read_csv())

total = 0
for item in data:
    total += item['cases']



print(total)
print(data[0])