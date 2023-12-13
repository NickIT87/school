a = True
b = False

def inverse():
    global a, b
    b = not b

inverse()

if a and b:
    print("a and b")
else:
    print("not working")

inverse()

if a and b:
    print("a and b")
else:
    print("not working")