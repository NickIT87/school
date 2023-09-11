# конструкція перехоплення помилок
a = 2
b = 0

#print(a / b)

try:
    print(a / b)            # проблемний код
except Exception as e:
    print(e)                # обробка помилки
finally:
    print("finished")