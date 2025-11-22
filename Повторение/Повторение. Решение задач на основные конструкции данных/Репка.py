a, b = [i for i in input().split(" -> ")], int(input())
for i in range(b):
    k = input()
    if a.index(k) == 0:
        print(f"{k} -> {a[a.index(k) + 1]}")
    elif a.index(k) == len(a) - 1:
        print(f"{a[a.index(k) - 1]} -> {k}")
    else:
        print(f"{a[a.index(k) - 1]} -> {k} -> {a[a.index(k) + 1]}")
