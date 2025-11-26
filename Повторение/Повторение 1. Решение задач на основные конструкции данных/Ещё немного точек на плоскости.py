n = int(input())
lst = []
le, r, t, b = 0, 0, 0, 0
minx, miny, maxx, maxy = 0, 0, 0, 0
for i in range(n):
    a = [int(i) for i in input().split()]
    if i == 0:
        le, r, t, b = tuple(a), tuple(a), tuple(a), tuple(a)
        minx, miny, maxx, maxy = a[0], a[1], a[0], a[1]
    else:
        if a[0] < minx:
            le = tuple(a)
            minx = a[0]
        if a[1] < miny:
            b = tuple(a)
            miny = a[1]
        if a[0] > maxx:
            r = tuple(a)
            maxx = a[0]
        if a[1] > maxy:
            t = tuple(a)
            maxy = a[1]
    if a[1] < abs(a[0]) and a[1] > -abs(a[0]):
        lst.append(tuple(a))
for i in lst:
    print(i)
print(f"left: {le}")
print(f"right: {r}")
print(f"top: {t}")
print(f"bottom: {b}")
