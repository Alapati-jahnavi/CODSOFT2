import tkinter as tk
from tkinter import messagebox
# Set up the main application window
root = tk.Tk()
root.title("Simple Calculator")
# Create the entry widget
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)
# Define button click functionality
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)
def button_clear():
    entry.delete(0, tk.END)
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid Input")
# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]
row_val = 1
col_val = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=9, height=3, command=button_equal).grid(row=row_val, column=col_val, columnspan=2)
    elif button == "C":
        tk.Button(root, text=button, width=9, height=3, command=button_clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=9, height=3, command=lambda x=button: button_click(x)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
# Run the application
root.mainloop()
