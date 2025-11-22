from math import *


a = input()
with open("function.txt", "w", encoding="utf-8") as f:
    st = 0.01
    x = 0.0
    c = 0
    while c < 201:
        f.write(str(x) + "\t" + str(round(eval(a), 3)) + "\n")
        x += st
        x = round(x, 3)
        c += 1
        