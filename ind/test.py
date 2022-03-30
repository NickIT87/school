
v_string: str = "hello"     # строка
v_integer: int = 12              # целое число
v_float: float = 14.7       # число с плавающей точкой 
v_bool: bool = True         # Булевы типы
# 1 = True  0 = False
v_list: list = ["1", 2, 3, True]    # список - изменяемый тип данных
v_tuple: tuple = (1, 2, 3, 4)       # кортеж - константа (не изменяемый тип данных)
v_set: set = {1, 2, 3, 4}           # множества элементов
v_dict: dict = {
    "Age": 12,
    "Name": "Arina",
    "Class": "5a"
}

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

