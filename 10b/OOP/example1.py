class Car:
    def __init__(self, b):
        self.__b = b

    def get_b(self):
        return self.__b

ob = Car(2)
ob.__b = 4


print(ob.get_b())
print(ob.__b, type(ob.__b))
print(ob.get_b())
