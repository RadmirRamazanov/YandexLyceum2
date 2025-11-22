import csv
from math import *


V = 60
with open("schedule.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    c = 0
    for row in reader:
        if not c:
            c += 1
            continue
        print(row[1] + "\t" + str(floor(V * int(row[2]) + V * int(row[3]) / 60)))
