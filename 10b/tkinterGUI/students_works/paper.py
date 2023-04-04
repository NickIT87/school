from tkinter import *

root = Tk()

canv = Canvas(root, width=500, height=500, bg="light yellow")
canv.pack()

canv.create_polygon(250, 190, 140, 280, 360, 280, fill="green", outline="black")
canv.create_polygon(250, 150, 170, 220, 330, 220, fill="green", outline="black")
canv.create_polygon(250, 110, 200, 160, 300, 160, fill="green", outline="black")
canv.create_rectangle(230, 280, 270, 330, fill="brown")
canv.create_text(252, 392, text="Happy New Year!", font="Times 30 italic", fill="darkred", justify=CENTER)
canv.create_text(250, 390, text="Happy New Year!", font="Times 30 italic", fill="red", justify=CENTER)

root.mainloop()