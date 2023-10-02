import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.root.title("undefined")
        width, height = 584, 195
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

    def create_button(self, text, x, y, width, height, command):
        button = tk.Button(self.root, text=text, bg="#efefef", font=tkFont.Font(family='Times', size=10),
                           fg="#000000", justify="center", command=command)
        button.place(x=x, y=y, width=width, height=height)
        return button


    def create_label(self, text, x, y, width, height):
        label = tk.Label(self.root, text=text, font=tkFont.Font(family='Times', size=10), fg="#333333", bg="#FFFFFF",
                        justify="center")
        label.place(x=x, y=y, width=width, height=height)
        return label


    def create_entry(self, x, y, width, height):
        entry = tk.Entry(self.root, borderwidth="1px", font=tkFont.Font(family='Times', size=16),
                         fg="#333333", justify="center")
        entry.place(x=x, y=y, width=width, height=height)
        return entry

    def create_widgets(self):
        self.view_button = self.create_button("View Records", 20, 130, 139, 30, self.view_records)
        self.add_button = self.create_button("Add Record", 210, 130, 142, 30, self.add_record)
        self.delete_button = self.create_button("Delete Record", 400, 130, 160, 30, self.delete_record)
        
        self.name_label = self.create_label("Enter Name:", 230, 20, 70, 25)
        self.name_entry = self.create_entry(140, 70, 248, 30)

    def view_records(self):
        print("View Records command")

    def add_record(self):
        print("Add Record command")

    def delete_record(self):
        print("Delete Record command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
