from tkinter import *


def add(eve):
    a = int(input("a: "))
    b = int(input("b: "))
    print(a + b)

def multiply(fff):
    c = int(input("c: "))
    d = int(input("d: "))
    print(c * d)

root = Tk()

but1 = Button(
    root,
    width = 15,
    height = 2,
    background = "blue",
    fg = "white"
)
but1['text'] = 'adding'
but1.bind("<Button>", add)

but2 = Button(root)
but2['text'] = 'multiply'
but2.bind("<Button>", multiply)

but1.pack()
but2.pack()

root.mainloop()