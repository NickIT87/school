import tkinter as tk

def button_clicked():
    print("Button Clicked")

root = tk.Tk()
button = tk.Button(root, text="Click me", command=button_clicked)
button.pack()
root.mainloop()
