from tkinter import *

root = Tk()
var1 = StringVar()
var2 = StringVar()
prap1 = Checkbutton( root, text="First", variable=var1, onvalue="first activated", offvalue="first deactivated")
prap2 = Checkbutton( root, text="Second", variable=var2, onvalue="second activated", offvalue="second deactivated")
lis = Listbox( root, bg="blue", height=3)

def func1(ven):
    v1 = var1.get()
    v2 = var2.get()
    l = [v1, v2]
    lis.delete(0, 1)
    for i in l:
        lis.insert(END, i)

but = Button(root, text="checkbox status")
but.bind('<Button-1>', func1)
prap1.deselect()
prap2.deselect()
prap1.pack()
prap2.pack()
but.pack()
lis.pack()
root.mainloop()
