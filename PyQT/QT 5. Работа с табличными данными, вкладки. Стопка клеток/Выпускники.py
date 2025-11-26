import csv


def prof(a):
    with open("vps.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for i in reader:
            try:
                if int(i[4]) >= a:
                    print(i[0])
            except ValueError:
                pass


prof(int(input()))