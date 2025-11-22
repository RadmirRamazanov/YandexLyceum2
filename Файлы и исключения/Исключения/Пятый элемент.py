with open("elements.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    summ = 0
    nums = []
    try:
        a, b, c, d = int(lines[0]), int(lines[1]), int(lines[2]), int(lines[3])
    except ValueError:
        print(0)
    except IndexError:
        print(1000)
    else:
        print(abs(a - d) + abs(b - c))
    finally:
        print("The fifth element has been found!")

