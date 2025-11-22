import math


try:
    x, y = [int(i) for i in input().split()]
    if x < 0 or y < 0:
        print("Negative sun height.")
    else:
        tg = x / y
        print(int(round(math.degrees(math.atan(tg)), 0)))
except ValueError as e:
    print(f"Wrong input data: {e}")
    