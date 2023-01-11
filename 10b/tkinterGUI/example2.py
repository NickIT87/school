from tkinter import *


class Kl9_04:
    def __init__(self, a, b, c, d):
        self.s = a + b
        self.p = c * d
        self.but1 = Button(root)
        self.but1['text'] = 'Додавання'
        self.but1.pack()
        self.but2 = Button(root)
        self.but2['text'] = 'Множення'
        self.but2.pack()
        self.but1.bind("<Button-1>", self.func1)
        self.but2.bind("<Button-1>", self.func2)

    def func1(self, rkt):
        print("a+b = ", self.s)

    def func2(self, rkt):
        print("c*d = ", self.p)

root = Tk()
obj = Kl9_04(3, 9, 6, 7)
root.mainloop()
