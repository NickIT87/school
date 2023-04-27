import turtle

# Define the L-System rules
# Define the initial string and number of iterations

# 1 Tree:

# rules = {'F': 'FF', 'X': 'F-[[X]+X]+F[+FX]-X'}
# axiom = 'X'
# n = 4

# 2 Koch Curve:

# rules = {'F': 'F+F-F-F+F'}
# axiom = 'F'
# n = 4

# 3 Dragon Curve:

# rules = {'X': 'X+YF+', 'Y': '-FX-Y'}
# axiom = 'FX'
# n = 12

# 4 Sierpinski Triangle:

rules = {'F': 'G-F-G', 'G': 'F+G+F'}
axiom = 'F'
n = 10


def apply_rules(s):
    return ''.join(rules.get(c, c) for c in s)

def iterate(s, n):
    for _ in range(n):
        s = apply_rules(s)
    return s

def draw_lsystem(s, angle, distance):
    stack = []
    for c in s:
        if c == 'F':
            turtle.forward(distance)
        elif c == '+':
            turtle.right(angle)
        elif c == '-':
            turtle.left(angle)
        elif c == '[':
            stack.append((turtle.position(), turtle.heading()))
        elif c == ']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()
            


# Generate the L-System string and draw the fractal
lsystem = iterate(axiom, n)
turtle.speed('fastest')
turtle.penup()
turtle.goto(0, -100)
turtle.setheading(90)
turtle.pendown()

# 1
# draw_lsystem(lsystem, 25, 15)

# 2 
# draw_lsystem(iterate(axiom, n), 90, 5)

# 3
# draw_lsystem(iterate(axiom, n), 90, 5)

# 4
draw_lsystem(iterate(axiom, n), 120, 5)

turtle.done()