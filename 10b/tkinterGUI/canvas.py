import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.create_line(0, 0, 200, 200)
canvas.create_rectangle(50, 50, 150, 150)
canvas.pack()
root.mainloop()
