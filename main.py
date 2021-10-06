from PIL import Image, ImageFilter

im = Image.open("mini messi.jpg")
print(im.format, im.size, im.mode)
im.show()
izmers = (1080, 1920)
im.thumbnail(izmers)
im.save("bilde-maza.jpg", im.format)
im.show()
im = im.rotate(360)
r, g, b = im.split()
im = Image.merge("RGB", (g,r,b))
im = im.filter(ImageFilter.BLUR)
im.show()
im = im.filter(ImageFilter.GaussianBlur)
im.show()


