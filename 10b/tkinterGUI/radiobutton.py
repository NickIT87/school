import tkinter as tk

root = tk.Tk()
var = tk.StringVar(value="Option 1")
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1")
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2")
radiobutton1.pack()
radiobutton2.pack()
root.mainloop()
