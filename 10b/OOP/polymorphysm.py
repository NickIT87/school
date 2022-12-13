class Bird:
    def info(self):
        print('This is a bird')
    # describe some functionality
    def flight(self):
        print("Most of the birds can fly but some cannot.")

# уарабей
class Sparrow(Bird):
    # give some information
    def flight(self):
        print("Sparrows can fly.")
        return True


class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
        return False

obj_spr = Sparrow()
obj_ost = Ostrich()
obj_spr.info()

if obj_spr.flight():         # True
    print("Уарабей летить")
if obj_ost.flight():        # False
    pass
else:
    print("Страус не урабей!")