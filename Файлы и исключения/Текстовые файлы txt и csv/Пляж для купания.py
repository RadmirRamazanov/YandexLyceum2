import csv


with open("beaches.csv", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    c = 0
    for row in reader:
        if not c:
            c += 1
            continue
        if int(row[2]) and int(row[3]) and float(row[4]) <= 0.5 and int(row[5]) >= 18:
            print(row[1])

