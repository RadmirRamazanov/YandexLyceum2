import csv


def resheto_eratosfena(n):
    p = [True] * (n + 1)
    p[0], p[1] = False, False
    c = 2
    while c * c <= n:
        if p[c]:
            for i in range(c * c, n + 1, c):
                p[i] = False
        c += 1
    ans = []
    for i in range(1, len(p)):
        if p[i] and n % i == 0 and len(ans) <= 4:
            ans.append(str(i))
    return ans


a, b = int(input()), int(input())
with open("divisors.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=" ")
    writer.writerow(["number", "div1", "div2", "div3", "div4", "div5"])
    for i in range(a, b + 1):
        writer.writerow([str(i), *resheto_eratosfena(i)])
