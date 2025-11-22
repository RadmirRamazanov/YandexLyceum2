with open("data.bin", "rb") as f1, open("part.dat", "wb") as f2:
    f2.write(f1.read(100))

