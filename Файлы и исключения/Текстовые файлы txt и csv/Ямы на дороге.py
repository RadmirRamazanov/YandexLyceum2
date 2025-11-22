import csv


with open("holes.csv", "w", encoding="utf-8", newline="") as f:
    a = int(input())
    n = int(input())
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["no", "kilometer", "stripe", "area", "depth", "priority"])
    for i in range(1, n + 1):
        d = [int(i) for i in input().split()]
        if d[-2] * d[-1] > a:
            writer.writerow([str(i), str(d[0]), str(d[1]), str(d[2]), str(d[3]), "1"])
        else:
            writer.writerow([str(i), str(d[0]), str(d[1]), str(d[2]), str(d[3]), "0"])
            