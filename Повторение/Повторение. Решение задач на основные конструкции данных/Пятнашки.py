from PIL import Image


im = Image.open("image.bmp")
x, y = im.size
new_x, new_y = x // 4, y // 4
t, r, b, le = 0, new_x, new_y, 0
for i in range(1, 5):
    for j in range(1, 5):
        if i == 4 and j == 4:
            break
        im.crop((le, t, r, b)).save("image" + str(i) + str(j) + ".bmp")
        le += new_x
        r += new_x
    t += new_y
    b += new_y
    le, r = 0, new_x

