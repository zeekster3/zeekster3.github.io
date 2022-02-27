from PIL import Image

beach = Image.open("beach.jpg")
cactus = Image.open("cactus.jpg")

cactus_pixel = cactus.load()
beach_pixel = beach.load()
(width, height) = cactus.size

for y in range(0, height):
    for x in range(0, width):
        r, g, b = cactus_pixel[x, y]
        if r <= 70 and g >= 250 and b <= 25: 
            cactus_pixel[x, y] = beach_pixel[x, y]

cactus.show()
cactus.save("beach_with_cactus.jpg")