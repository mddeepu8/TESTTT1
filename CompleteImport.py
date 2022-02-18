#importing complete csv
import csv
with open('new1.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)