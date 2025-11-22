with open("black/another_black/cats_black_and_other.txt", "r", encoding="utf-8") as f1, \
        open("cats.txt", "w", encoding="utf-8") as f2:
    lines = f1.readlines()
    cat_lines = []
    words = []
    for i in lines:
        if "cat" in i.lower():
            cat_lines.append(i)
    for i in cat_lines:
        i = i.split()
        for j in i:
            if len(j) > 1:
                if j[0].isupper() and j[1].islower():
                    words.append(j)
            else:
                if j[0].isupper():
                    words.append(j)
    words.sort()
    for i in words:
        f2.write(i + "\n")

