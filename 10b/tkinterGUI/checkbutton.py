import tkinter as tk

root = tk.Tk()
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
checkbutton1 = tk.Checkbutton(root, text="Option 1", variable=var1)
checkbutton2 = tk.Checkbutton(root, text="Option 2", variable=var2)
checkbutton1.pack()
checkbutton2.pack()
root.mainloop()
