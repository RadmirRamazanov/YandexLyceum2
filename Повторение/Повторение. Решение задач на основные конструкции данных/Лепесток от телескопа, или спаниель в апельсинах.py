import sys


a, data = input(), list(map(str.strip, sys.stdin))
ans, lst = 0, []
for i in data:
    k = 0
    d_a = list(a)
    for j in i:
        if j in d_a:
            k += 1
            d_a.remove(j)
    if k == len(i):
        ans += 1
        lst.append(i)
print(ans)
for i in lst:
    print(i)
    