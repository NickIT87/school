import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=584
        height=195
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_533=tk.Button(root)
        GButton_533["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_533["font"] = ft
        GButton_533["fg"] = "#000000"
        GButton_533["justify"] = "center"
        GButton_533["text"] = "View Records"
        GButton_533.place(x=20,y=130,width=139,height=30)
        GButton_533["command"] = self.GButton_533_command

        GButton_10=tk.Button(root)
        GButton_10["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_10["font"] = ft
        GButton_10["fg"] = "#000000"
        GButton_10["justify"] = "center"
        GButton_10["text"] = "Add Record"
        GButton_10.place(x=210,y=130,width=142,height=30)
        GButton_10["command"] = self.GButton_10_command

        GButton_907=tk.Button(root)
        GButton_907["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_907["font"] = ft
        GButton_907["fg"] = "#000000"
        GButton_907["justify"] = "center"
        GButton_907["text"] = "Delete Record"
        GButton_907.place(x=400,y=130,width=160,height=30)
        GButton_907["command"] = self.GButton_907_command

        GLabel_190=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_190["font"] = ft
        GLabel_190["fg"] = "#333333"
        GLabel_190["justify"] = "center"
        GLabel_190["text"] = "Enter Name:"
        GLabel_190.place(x=230,y=20,width=70,height=25)

        GLineEdit_41=tk.Entry(root)
        GLineEdit_41["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_41["font"] = ft
        GLineEdit_41["fg"] = "#333333"
        GLineEdit_41["justify"] = "center"
        GLineEdit_41["text"] = "Entry"
        GLineEdit_41.place(x=140,y=70,width=248,height=30)

    def GButton_533_command(self):
        print("command")


    def GButton_10_command(self):
        print("command")


    def GButton_907_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
