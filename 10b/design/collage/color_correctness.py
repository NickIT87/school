from PIL import Image, ImageEnhance


# Відкриваємо зображення
img = Image.open('image.jpeg')

# Виконуємо тонову корекцію зображення
enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(1.2)

# Виконуємо корекцію кольору зображення
enhancer = ImageEnhance.Color(img)
img = enhancer.enhance(1.5)

# збільшення контрасту
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.5)

# Зберігаємо зображення
img.save('processed_image.jpg')
