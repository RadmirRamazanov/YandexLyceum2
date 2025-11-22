import csv


with open("strikes.csv", "r", encoding="utf-8") as f1, open("predict.csv", "w", encoding="utf-8", newline="") as f2:
    reader = csv.reader(f1, delimiter="\t")
    writer = csv.writer(f2, delimiter=";")
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    matrix = []
    x, y = 0, 0
    for i in reader:
        x += 1
        y = len(i)
        matrix.append(i)
    print(matrix)
    for i in range(x):
        row = []
        for j in range(y):
            a, b = 0, 0
            for nx, ny in neighbors:
                dx, dy = i + nx, j + ny
                if dx >= 0 and dx < x and dy >= 0 and dy < y:
                    a += 1
                    if matrix[dx][dy] == '1':
                        b += 1
            if matrix[i][j] == '1':
                if b / a - 0.1 >= 0:
                    row.append(round(b / a - 0.1, 3))
                else:
                    row.append(round(b / a, 3))
            else:
                row.append(round(b / a, 3))
        writer.writerow(row)
