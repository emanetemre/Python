import csv

file = open("account.csv")
reader = csv.reader(file, delimiter=",")

for row in reader:
    print(row)
    print("")