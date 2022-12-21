import matplotlib.pyplot as plt


def fibonacci_ser(m: int) -> int:
    if(m <= 1):
        return m
    else:
        return fibonacci_ser(m-1) + fibonacci_ser(m-2)


data = []
for i in range(30):
    data.append(fibonacci_ser(i))

print(data)

# plt.plot(data)
# plt.show()

# from math import pi, sin, cos
# import turtle
# import time

# time.sleep(2)

# screen = turtle.Screen()
# turtle.shape('turtle')
# for i in range(17):
#     t = i / 2 * pi
#     dx = data[i] * cos(t)
#     dy = data[i] * sin(t)
#     turtle.goto(dx, dy)

# screen.exitonclick()