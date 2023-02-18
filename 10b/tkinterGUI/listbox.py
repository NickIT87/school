import tkinter as tk

def listbox_selection(event):
    selection = event.widget.curselection()
    print(event.widget.get(selection[0]))

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.bind("<<ListboxSelect>>", listbox_selection)
listbox.pack()
root.mainloop()
