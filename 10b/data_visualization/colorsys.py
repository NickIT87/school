from colorsys import rgb_to_cmyk

# Зелений колір в RGB
r, g, b = 0, 255, 0

# Конвертування в модель CMYK
c, m, y, k = rgb_to_cmyk(r/255, g/255, b/255)

# Друк кольорів в обох моделях
print(f"RGB: ({r}, {g}, {b})")
print(f"CMYK: ({int(c*100)}, {int(m*100)}, {int(y*100)}, {int(k*100)})")
