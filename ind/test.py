import time
from math import sqrt

from numpy import number


print(sqrt(4)) # вычисление квадратного корня числа


v_string: str = "hello"                 # строка
v_integer: int = 12                     # целое число
v_float: float = 14.7                   # число с плавающей точкой 
v_bool: bool = False                    # Булевы типы
# 1 = True  0 = False
v_list: list = ["1", 2, 3.6, True]      # список - изменяемый тип данных
a = v_list[:2]                          # срез списка
v_tuple: tuple = (1, 2, 3, 4)           # кортеж - константа (не изменяемый тип данных)
v_set: set = {1, 2, 3, 4}               # множества элементов
b = set('Hello')                        # создание неупорядоченного множества
v_dict: dict = {
    "Age": 12,
    "Name": "Arina",
    "Class": "5a"
}
v_none = None
# двумерный список
two_dimensional_list: list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Тема ООП - объектно ориентированное программирование
class Student:
    def __init__(self, name, age, c_num):
        self.name = name
        self.age = age
        self.class_number = c_num

    def say(self):
        print("hello my name is ", self.name)


s1 = Student("Arina", 12, "5a")
s2 = Student("Ivan", 13, "5b")


print(s1.say())         # вызов приветствия у студента № 1
print(s2.say())         # вызов приветствия у студента № 2
print(v_list[1], len(v_list))
print(v_dict["Name"])


# проверка типа данных
print(len(v_list))      # проверка длины списка
print(type(v_integer)) 
a = 123
b = '123'
z = 'sdfgsdfgsdgsdfg'
# преобразования данных
print(type(int(b))) 
print(type(str(a)))
print(''.join(list(z)), list(z))


# ветвление  Основная конструкция
trigger1 = None
if( trigger1 == 12 ):
    print("выполнено главное условие if")
elif ( trigger1 != 12 and trigger1 != None ):
    print("второе условие if")
else:
    print("третье условие if ")


# ветвление не основная конструкция
trigger2 = None
match trigger2:
    case "abc": 
        print("Первое условие match")
    case "2":
        print("Второе условие match")
    case None:
        print("условие не выполнено")


# циклы
for i in v_list:
    print(type(i))
    if (type(i) == bool):
        i = False
        print (i)


for i in range(len(v_list)):
    v_list[i] = i 
    print(i)
    #time.sleep(1)
print(v_list)

i = 0
while True:
    i += 1
    print(i)
    #time.sleep(0.5)
    if i > 10:
        break


# создание функций
def abs(number: int) -> number:
    return number if number >= 0 else -number


print(abs(-123)) # простейшая функция которая возвращает модуль числа


#алгоритм сортировки

unsorted_list = [3, 5, 7, 1, 2, 45, 12, 54]
unsorted_list.sort()
unsorted_list.reverse()
print(unsorted_list)