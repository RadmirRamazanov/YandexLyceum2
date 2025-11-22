dct = {}
while True:
    try:
        a = [i for i in input().split("\t")]
        dct[a[0]] = a[1]
    except IndexError:
        break
while True:
    try:
        try:
            a = [i for i in input().split()]
            k = a[0]
        except IndexError:
            break
        c = " ".join(a)
        print(dct[c])
    except KeyError:
        print("Делай, что должен, и будь, что будет.")
