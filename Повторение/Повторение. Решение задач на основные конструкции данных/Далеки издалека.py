import sys


data = list(map(str.strip, sys.stdin))
ans = 0
for i in data:
    h = i.split()
    for j in h:
        j = j.lower()
        if j[:5] == "далек":
            ans += 1
            break
print(ans)
