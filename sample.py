import csv
with open(r"C:\Users\Deepak M\Desktop\pythonProject2\practice\input.csv",'r') as f1:
    rows = csv.reader(f1)
    for row in rows:
        if len(row) < 5:
            print("invalid data",row)
        for i in row:
            if i == '0':
                print(row)





