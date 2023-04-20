from colorama import Fore, Style

# Зелений колір в RGB
r, g, b = 0, 255, 0

# Друк кольорової моделі RGB
print(f"RGB: {Fore.RED}{r}{Style.RESET_ALL}, {Fore.GREEN}{g}{Style.RESET_ALL}, {Fore.BLUE}{b}{Style.RESET_ALL}")


# Червоний колір в RGB
r1, g1, b1 = 255, 0, 0

# Зелений колір в RGB
r2, g2, b2 = 0, 255, 0

# Змішування кольорів
r3 = min(r1 + r2, 255)
g3 = min(g1 + g2, 255)
b3 = min(b1 + b2, 255)

# Друк змішаного кольору в RGB
print(f"Mixed color: ({r3}, {g3}, {b3})")
