import sys


data = list(map(str.split, sys.stdin))
raspisanie = {}
for i in data:
    if len(i) > 1:
        if int(i[-1]) not in raspisanie:
            raspisanie[int(i[-1])] = []
            raspisanie[int(i[-1])].append(" ".join(i[:-1]))
        else:
            if " ".join(i[:-1]) not in raspisanie[int(i[-1])]:
                raspisanie[int(i[-1])].append(" ".join(i[:-1]))
for k, i in sorted(raspisanie.items()):
    print(f"{k}:", ", ".join(i))
    