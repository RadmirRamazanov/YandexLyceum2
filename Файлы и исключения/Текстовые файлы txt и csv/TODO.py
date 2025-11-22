with open("todo.txt", "r", encoding="utf-8") as f1, open("no_repeat.txt", "w", encoding="utf-8") as f2:
    lines = f1.readlines()
    lines = set(lines)
    for i in lines:
        f2.write(i)
