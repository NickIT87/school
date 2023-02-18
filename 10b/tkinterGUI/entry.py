import tkinter as tk

def entry_changed(event):
    print(event.widget.get())

root = tk.Tk()
entry = tk.Entry(root)
entry.bind("<KeyRelease>", entry_changed)
entry.pack()
root.mainloop()
