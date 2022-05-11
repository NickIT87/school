from fractions import Fraction

a = Fraction('1/2')     # рациональные числа
b = Fraction(1, 2)
d = Fraction('123.2')
c = a + b
#print(float(c))

# Барвінок зібрав у своєму садочку 456.3 кг. яблук і груш. 
# Яблука він розклав у 9 ящиків по 23.5 кг. у кожний
# а груші порівну у 12 кошиків.
# Скільки кг. груш було в кожному кошику?


# all_fruits = 456.3
# one_apple_box = 23.5
# all_apples = one_apple_box * 9
# print("Усього яблук: ", all_apples)
# all_pears = all_fruits - all_apples
# one_pear_box = all_pears / 12
# print(one_pear_box)
# print(Fraction('20.4'))

# Калькулятор для барвинка!
a_f = input("Введіть кількість фруктів: ")
apl_box_size = input("Введіть об'єм ящика: ")
cnt_apl_box = input("Введіть кількість ящиків в наявності для яблук: ")
apples = input("Введіть кількість яблук: ")

box_need = int(apples) / int(apl_box_size)

if box_need <= int(cnt_apl_box):
    print("ящиків достатньо")
else:
    print("не вистачає")


