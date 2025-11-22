import sys


data = list(map(str.strip, sys.stdin))
ans = 0
for i in data:
    h = i.split()
    for j in h:
        j = j.lower()
        if "далек" in j:
            ans += 1
            break
print(ans)
