import datetime as dt


h = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]
h.sort()
m.sort()
for i in h:
    for j in m:
        if sum(map(int, str(i))) != sum(map(int, str(j))):
            print(dt.time(i, j).strftime("%H:%M"))
            