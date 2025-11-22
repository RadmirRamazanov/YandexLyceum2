a, b = input(), int(input())
k = b % len(a)
d = a[k:] + a[:k]
new_al = a[-k:] + a[:-k]
print(d)
print(a)
print(new_al)
