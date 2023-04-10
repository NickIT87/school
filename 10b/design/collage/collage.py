from PIL import Image

# Зчитуємо зображення
image1 = Image.open('image2.jpg')
image2 = Image.open('image2.jpg')
image3 = Image.open('image2.jpg')

# Визначаємо розміри колажу та створюємо нове зображення
width, height = image1.size
collage_width = width * 3
collage_height = height
collage = Image.new('RGB', (collage_width, collage_height))

# Розміщуємо зображення у колажі
collage.paste(image1, (0, 0))
collage.paste(image2, (width, 0))
collage.paste(image3, (width * 2, 0))

# Зберігаємо колаж
collage.save('collage.jpg')
