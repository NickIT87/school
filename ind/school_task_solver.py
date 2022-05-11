# task 1
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


# task 2
# довжина побудованої дороги становить 92 км.
# за перший місяц побудували 6/23 дороги, а 
# за другий місяць 9/23. 
# Скільки кілометрів було побудовано за 2 місяці. 

# from fractions import Fraction
# road_length = 92
# first_month = Fraction(15, 23)
# second_month = Fraction(7, 23)
# two_month_length_total = first_month + second_month
# print(two_month_length_total)
# print(road_length / two_month_length_total.denominator * two_month_length_total.numerator)


import nums_from_string
from fractions import Fraction


road_length = int(input("Введіть загальну довжину дороги: "))
total_month_counter = int(input("Введіть кількість місяців протягом яких будували дорогу: "))
total_month_data = []
total_month_data_list = []
total_month_fractions = []

for i in range(total_month_counter):
    total_month_data.append(input("Введіть значення дробі для місяця {}: ".format(i)))

for i in total_month_data:
    total_month_data_list.append(nums_from_string.get_nums(i))

for i in total_month_data_list:
    total_month_fractions.append(Fraction(i[0], i[1]))

total_builded_road = sum(total_month_fractions)
print(road_length / total_builded_road.denominator * total_builded_road.numerator)
