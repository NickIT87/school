# koch snowflake example
import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

# Set up the turtle
t = turtle.Turtle()
t.speed('fastest')

# Draw the Koch snowflake
for i in range(3):
    koch_snowflake(t, 4, 200)
    t.right(120)

# Hide the turtle when finished
t.hideturtle()

# Keep the window open
turtle.done()