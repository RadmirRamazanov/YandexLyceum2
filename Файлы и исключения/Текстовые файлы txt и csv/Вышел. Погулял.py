with open("poem.txt", "r", encoding="utf-8") as f1:
    lines = f1.readlines()
    with open("counting.txt", "w", encoding="utf-8") as f2:
        c = 1
        for i in lines:
            f2.write(f"{str(c)} - {i}")
            c += 1

