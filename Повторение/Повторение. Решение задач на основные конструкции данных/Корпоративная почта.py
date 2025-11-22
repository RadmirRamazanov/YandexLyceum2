n = int(input())
pochta = []
for i in range(n):
    a = input()
    pochta.append(a[:a.find("@")])
m = int(input())
for i in range(m):
    a = input()
    if a in pochta:
        k = 1
        while a in pochta:
            if k == 1:
                a += str(k)
            else:
                a = list(a)
                a[-1] = str(k)
                a = "".join(a)
            k += 1
    print(a + "@untitled.py")
    pochta.append(a)
    