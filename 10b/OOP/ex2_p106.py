class K18_16:
    def __init__(self, a1, a2):
        try:
            self.z = a1 / a2
        except:
            raise Exception("Sorry, no numbers below zero")
        else:
            print("result = ", self.z)
        finally:
            print("end programm")

#K18_16(2, 0)


class K18_18(Exception):
    def __init__(self, a1, a2):
        Exception.__init__(self)
        self.p1 = a1
        self.p2 = a2


K = int(input("Сума вкладу: "))

try:
    x = int(input("Яку сумму зняти? "))
    if x > K:
        raise K18_18(x, K)
except K18_18 as t1:
    print('Зняти суму {0} не можна'.format(t1.p1))
    print('на рахунку залишається ', K)
else:
    s = K - x
    print("Знято ", x, "Залишок ", s)
finally:
    print("програма завершена")