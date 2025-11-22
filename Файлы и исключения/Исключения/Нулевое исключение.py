a = int(input())
b = int(str(a)[0])
for i in str(a)[1:]:
    b *= int(i)
try:
    print(a / b)
except ZeroDivisionError:
    print(0)

