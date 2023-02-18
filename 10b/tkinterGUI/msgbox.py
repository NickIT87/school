import tkinter as tk
from tkinter import messagebox

def button_clicked():
    messagebox.showinfo("Info", "Hello World")

root = tk.Tk()
button = tk.Button(root, text="Click me", command=button_clicked)
button.pack()
root.mainloop()
