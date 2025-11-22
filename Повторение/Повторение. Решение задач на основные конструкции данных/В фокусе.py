from PIL import Image, ImageChops


im = Image.open("image.png")
pixels = im.load()
fon = pixels[0, 0]
im_new = Image.new("RGB", im.size, fon)
bez_fona = ImageChops.difference(im_new, im).getbbox()
im.crop(bez_fona).save("res.png")
