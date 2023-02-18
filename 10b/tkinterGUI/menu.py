import tkinter as tk

def menu_file_new():
    print("New File")

root = tk.Tk()

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=menu_file_new)
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
