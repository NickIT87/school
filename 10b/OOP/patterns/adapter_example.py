import math

# Класи з сумісними інтерфейсами: КруглийОтвір та
# КруглийКілочок.
class RoundHole:
    def __init__(self, radius: int):
        self.radius: int = radius

    def getRadius(self) -> int:
        # Повернути радіус отвору.
        return self.radius

    def fits(self, peg: 'RoundPeg'):
        return self.getRadius() >= peg.getRadius()


class RoundPeg:
    def __init__(self, radius: int):
        self.radius: int = radius

    def getRadius(self) -> int:
        # Повернути радіус круглого кілочка.
        return self.radius


# Застарілий несумісний клас: КвадратнийКілочок.
class SquarePeg:
    def __init__(self, width: int):
        self.width: int = width

    def getWidth(self) -> int:
        # Повернути ширину квадратного кілочка.
        return self.width


# Адаптер дозволяє використовувати квадратні кілочки й круглі
# отвори разом.
class SquarePegAdapter(RoundPeg):
    __peg: SquarePeg

    def __init__(self, peg: SquarePeg):
        self.__peg: SquarePeg = peg

    def getRadius(self):
        # Обчислити половину діагоналі квадратного кілочка за
        # теоремою Піфагора.
        return self.__peg.getWidth() * math.sqrt(2) / 2


# Десь у клієнтському програмному коді.
hole = RoundHole(5)
rpeg = RoundPeg(5)
print("hole.fits(rpeg): ", hole.fits(rpeg)) # TRUE

small_sqpeg = SquarePeg(5)
large_sqpeg = SquarePeg(10)
#hole.fits(small_sqpeg) # Помилка компіляції, несумісні типи.

small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
print('hole.fits(small_sqpeg_adapter): ', hole.fits(small_sqpeg_adapter)) # TRUE
print("hole.fits(large_sqpeg_adapter): ", hole.fits(large_sqpeg_adapter)) # FALSE