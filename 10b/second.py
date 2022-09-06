class Student:
    def __init__(self, name, description):
        self.name = name
        self.description = description

s1 = Student('Nick', description="some description")


print(s1.name + " " + s1.description)