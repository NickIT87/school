import tkinter as tk
from tkinter import messagebox
import sqlite3
import logging


# Configure the logging module
logging.basicConfig(filename='my_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Create a connection to the database (or create one if it doesn't exist)
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS records
             (id INTEGER PRIMARY KEY, name TEXT)''')
conn.commit()

# Function to view all records
def view_records():
    c.execute('SELECT * FROM records')
    records = c.fetchall()
    for record in records:
        print(record)

# Function to add a new record
def add_record():
    name = entry.get()
    c.execute('INSERT INTO records (name) VALUES (?)', (name,))
    conn.commit()
    entry.delete(0, tk.END)
    messagebox.showinfo('Success', 'Record added successfully')
    logging.info(f'Added record {name}')

# Function to delete a record by ID
def delete_record():
    try:
        record_id = int(entry_id.get())
        c.execute('DELETE FROM records WHERE id = ?', (record_id,))
        conn.commit()
        entry.delete(0, tk.END)
        messagebox.showinfo('Success', 'Record deleted successfully')
        logging.info(f'record id: {record_id} deleted')
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid ID')
        logging.error('invalid id entered for deletion')

# Function to edit a record by ID
def edit_record():
    try:
        record_id = int(entry_id.get())
        name = entry.get()
        c.execute('UPDATE records SET name = ? WHERE id = ?', (name, record_id))
        conn.commit()
        messagebox.showinfo('Success', 'Record updated successfully')
        logging.info(f'record id: {record_id}, name: {name} edited successfully')
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid ID')
        logging.error('invalid id entered for editing')

# Create main window
root = tk.Tk()
root.title('SQLite3 GUI')

# Labels and entry fields
label = tk.Label(root, text='Enter Name:')
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

label_id = tk.Label(root, text='Enter record ID (for editing data):')
label_id.pack(pady=10)
entry_id = tk.Entry(root)
entry_id.pack(pady=10)

# Buttons for actions
view_button = tk.Button(root, text='View Records', command=view_records)
view_button.pack(padx=10, pady=10, side=tk.LEFT)

add_button = tk.Button(root, text='Add Record', command=add_record)
add_button.pack(padx=10, pady=10, side=tk.LEFT)

delete_button = tk.Button(root, text='Delete Record', command=delete_record)
delete_button.pack(padx=10, pady=10, side=tk.LEFT)

edit_button = tk.Button(root, text='Edit Record', command=edit_record)
edit_button.pack(padx=10, pady=10, side=tk.LEFT)

# Run the GUI application
root.mainloop()

# Close the connection when done
c.close()
conn.close()
