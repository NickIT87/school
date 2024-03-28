# import functools 
  
# # initializing list 
# lis = [1, 3, 5, 6, 2] 
  
# # using reduce to compute sum of list 
# print("The sum of the list elements is : ", end="") 
# print(functools.reduce(lambda a, b: a+b, lis)) 
  
# # using reduce to compute maximum element from list 
# print("The maximum element of the list is : ", end="") 
# print(functools.reduce(lambda a, b: a if a > b else b, lis)) 

# for i in range(1, len(lis)):
#     if lis[i] > lis[i-1]:
#         print(lis[i])
#     else:
#         print(lis[i-1])


from sympy import symbols, tan, sin, limit, pi

x = symbols('x')
expr = (x**3 - 3*x**2 + 5*x - 15) / (x**3 - 27)
lim_result = limit(expr, x, 3)
print(lim_result)

expr2 = (tan(x/2)) / (sin(x)**2)
lim_result2 = limit(expr2, x, pi, dir='+')  # approaching from the right
print(lim_result2)


import sympy as sp
# Визначення символьних змінних
x = sp.symbols('x')
# Вираз для функції
f = sp.atan(3*x**4) + 1/sp.sqrt(sp.sin(2*x)**3)
# Обчислення похідної
f_derivative = sp.diff(f, x)
# Виведення результату
print("Похідна функції:", f_derivative)


import sympy as sp
# Створення символьних змінних
x = sp.Symbol('x')
y = x * sp.ln(x)
# Знаходження похідної
dy_dx = sp.diff(y, x)
# Визначення точки перетину з Ox
x_intersect = 1
y_intersect = x_intersect * sp.ln(x_intersect)
# Обчислення нахилу дотичної в точці перетину
slope = dy_dx.subs(x, x_intersect)
# Визначення рівняння дотичної
# Формула: y - y1 = m(x - x1)
x1, y1 = x_intersect, y_intersect
equation_tangent = sp.Eq(y - y1, slope * (x - x1))
print("Рівняння дотичної:", sp.simplify(equation_tangent))
