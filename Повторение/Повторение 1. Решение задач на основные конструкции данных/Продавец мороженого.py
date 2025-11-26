n = int(input())
menu = {}
for i in range(n):
    a = [i for i in input().split()]
    menu[" ".join(a[:-1])] = int(a[-1])
k = input()
pokupki = {}
c = 1
ans = 0
u = []
while True:
    k = [i for i in input().split()]
    if len(k) != 0 and len(k) != 1:
        if c in pokupki:
            pokupki[c] += menu[" ".join(k[:-1])] * int(k[-1])
            ans += menu[" ".join(k[:-1])] * int(k[-1])
        else:
            pokupki[c] = menu[" ".join(k[:-1])] * int(k[-1])
            ans += menu[" ".join(k[:-1])] * int(k[-1])
    else:
        if len(k) == 0 and len(u) == 0:
            continue
        c += 1
    if len(k) == 1:
        break
    u = k
for k, i in pokupki.items():
    print(f"{k}) {i}")
print(f"Итого: {ans}")
