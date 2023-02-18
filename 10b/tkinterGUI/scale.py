import tkinter as tk

def scale_changed(value):
    print(value)

root = tk.Tk()
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=scale_changed)
scale.pack()
root.mainloop()
