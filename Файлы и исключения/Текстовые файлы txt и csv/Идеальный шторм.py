import csv


with open("storm.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    max_volna = 0
    volny = []
    for row in reader:
        if len(set(row)) == 5:
            c = 0
            for i in row:
                if int(i) % 2 == 0:
                    c += 1
            if c >= 3:
                volny.append(row)
        for i in row:
            if int(i) > max_volna:
                max_volna = int(i)
    min_volna = 1e9
    ans = 0
    new_volny = []
    for i in volny:
        for j in i:
            if j[-1] == str(max_volna)[-1]:
                ans += 1
                new_volny.append(i)
                break
    for i in new_volny:
        for j in i:
            if int(j) < min_volna:
                min_volna = int(j)
    print(ans, min_volna)

