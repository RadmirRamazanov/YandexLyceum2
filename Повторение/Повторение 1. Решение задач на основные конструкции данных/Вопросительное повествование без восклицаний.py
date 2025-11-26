import sys


data = list(map(str.strip, sys.stdin))
zxc = []
pov, vopr, voskl = set(), set(), set()
for i in data:
    a = ""
    for j in i:
        if j not in ".!?":
            a += j.lower()
        else:
            a += j
            zxc.append(a)
            a = ""
for i in zxc:
    a = ""
    for j in i:
        if j not in ".!?":
            a += j.lower()
        elif j == ".":
            a = a.split()
            for x in a:
                pov.add(x)
        elif j == "!":
            a = a.split()
            for x in a:
                voskl.add(x)
        elif j == "?":
            a = a.split()
            for x in a:
                vopr.add(x)
ans_lst = []
for i in pov:
    if i in vopr and i not in voskl:
        ans_lst.append(i)
ans_lst.sort()
print(*ans_lst)
