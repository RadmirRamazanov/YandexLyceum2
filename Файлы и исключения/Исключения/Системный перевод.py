import sys


data = list(map(str.strip, sys.stdin))
for i in data:
    i = i.split()
    try:
        print(f"{i[0]}({i[1]}) = {int(i[0], int(i[1]))}")
    except ValueError:
        pass
