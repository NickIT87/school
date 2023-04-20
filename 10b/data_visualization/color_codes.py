# RGB: 255, 0, 0
# Hex: #FF0000
# Binary: 11111111 00000000 00000000

binary_red = 0b11111111_00000000_00000000
print(binary_red)  # Виведе 16711680

# RGB: 0, 255, 0
# Hex: #00FF00
# Binary: 00000000 11111111 00000000

binary_green = 0b00000000_11111111_00000000
print(binary_green)  # Виведе 65280


# RGB: 0, 0, 255
# Hex: #0000FF
# Binary: 00000000 00000000 11111111

binary_blue = 0b00000000_00000000_11111111
print(binary_blue)  # Виведе 255


from PIL import Image

# Створити зображення розміром 1x1 з білим фоном
img = Image.new('RGB', (1, 1), color='white')

# Встановити червоний піксель на позиції (0, 0)
img.putpixel((0, 0), (255, 0, 0))  # (R, G, B)

# Зберегти зображення
img.save('red_pixel.png')

# Встановити зелений піксель на позиції (0, 0)
img.putpixel((0, 0), (0, 255, 0))  # (R, G, B)

# Зберегти зображення
img.save('green_pixel.png')

# Встановити синій піксель на позиції (0, 0)
img.putpixel((0, 0), (0, 0, 255))  # (R, G, B)

# Зберегти зображення
img.save('blue_pixel.png')
