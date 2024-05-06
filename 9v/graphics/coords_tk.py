import tkinter as tk

def motion(event):
    x, y = event.x, event.y
    label.config(text=f'X: {x}, Y: {y}')

# Create the tkinter window
root = tk.Tk()
root.title("Mouse Coordinates")

# Create a label to display coordinates
label = tk.Label(root, text="", font=("Helvetica", 16))
label.pack(pady=10)

# Bind mouse motion to the motion function
root.bind('<Motion>', motion)

# Run the tkinter event loop
root.mainloop()
