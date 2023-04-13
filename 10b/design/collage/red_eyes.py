from PIL import Image

img = Image.open('photo.jpg')
img = img.convert('RGB')  # перевод в RGB для работы с каналами цвета
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r, g, b = pixels[i, j]
        if r > 150 and g < 100 and b < 100:  # условие для красных глаз
            pixels[i, j] = (g, b, r)  # замена цветов

img.save('no_red_eye.jpg')
