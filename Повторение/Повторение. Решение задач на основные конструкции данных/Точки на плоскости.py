n = int(input())
lst = []
frst, scnd, thrd, frth = 0, 0, 0, 0
for i in range(n):
    a = [int(i) for i in input().split()]
    if a[0] == 0 or a[1] == 0:
        lst.append(tuple(a))
    if a[0] > 0 and a[1] > 0:
        frst += 1
    elif a[0] < 0 and a[1] > 0:
        scnd += 1
    elif a[0] < 0 and a[1] < 0:
        thrd += 1
    elif a[0] > 0 and a[1] < 0:
        frth += 1
for i in lst:
    print(i)
print(f"I: {frst}, II: {scnd}, III: {thrd}, IV: {frth}.")