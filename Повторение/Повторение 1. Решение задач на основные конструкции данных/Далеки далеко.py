import sys


data = list(map(str.strip, sys.stdin))
ans = 0
for i in data:
    h = i.split()
    for j in h:
        j = j.lower()
        if j == "далек" or j == "далека" or j == "далеку" or j == "далека" or j == "далеком" or j == "далеке" \
                or j == "далеки" or j == "далеков" or j == "далекам" or j == "далеков" or j == "далеками" or \
                j == "далеках":
            ans += 1
            break
print(ans)
