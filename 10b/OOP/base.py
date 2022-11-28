# Авто 15

# bmv, mersedes, audi

# bmv 5, 8

# mers 600, 500, S

# audi 1, 2, 3

# Інкапсуляція, Наслідування, Поліморфізм


class Car(object):
    price: float = None
    type = None


class BMV(Car):
    logo = "BMV"
    model: int = None

    def __init__(self, price, model, type):
        self.price = price
        self.model = model
        self.type = type


bmv = BMV(12335.35, 155, 'Truck')
bmv1 = BMV(12335.35, 5, 'sedan')

print(bmv.price, bmv.logo, bmv.model, bmv.type)
print(type(bmv))