import csv


def prof(a):
    with open("rez.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        school = []
        for i in reader:
            if i[0] == "place":
                continue
            i[2] = i[2].split("-")
            i[1] = i[1].split()
            if int(i[2][2]) == a[0] and int(i[2][3]) == a[1]:
                school.append([i[1][3], int(i[-1])])
        school.sort(key=lambda i: (i[1], i[0]), reverse=True)
        for i in school:
            print(" ".join(map(str, i)))


prof([int(i) for i in input().split()])