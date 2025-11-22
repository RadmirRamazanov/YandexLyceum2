n = ""
k = 0
try:
    for i in range(6):
        a = input()
        n += a[(len(a) - 1) // 2]
        k += 1
except EOFError:
    print(f"Error EOF, {k} of lines entered.")
else:
    print(n)

