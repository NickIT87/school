class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        return "Hello, my name is " + self.name


s1 = Student("Petro", 15)
s2 = Student("Vasyl", 14)

print(s2.hello())