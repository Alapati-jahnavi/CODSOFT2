import secrets
import string
import tkinter as tk
from tkinter import messagebox
def generate_secure_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True, exclude_similar=False):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters for better security.")
    character_sets = {
        'uppercase': string.ascii_uppercase,
        'lowercase': string.ascii_lowercase,
        'digits': string.digits,
        'special': string.punctuation
    }
    characters = ''
    if use_uppercase:
        characters += character_sets['uppercase']
    if use_lowercase:
        characters += character_sets['lowercase']
    if use_digits:
        characters += character_sets['digits']
    if use_special:
        characters += character_sets['special']
    if exclude_similar:
        similar_chars = '0O1lI'
        characters = ''.join(ch for ch in characters if ch not in similar_chars)
    if not characters:
        raise ValueError("No character types selected.")
    password = []
    if use_uppercase:
        password.append(secrets.choice(character_sets['uppercase']))
    if use_lowercase:
        password.append(secrets.choice(character_sets['lowercase']))
    if use_digits:
        password.append(secrets.choice(character_sets['digits']))
    if use_special:
        password.append(secrets.choice(character_sets['special']))
    while len(password) < length:
        password.append(secrets.choice(characters))
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)
def generate_password():
    try:
        length = int(length_var.get())
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()
        exclude_similar = similar_var.get()
        password = generate_secure_password(length, use_uppercase, use_lowercase, use_digits, use_special, exclude_similar)
        result_var.set(password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
# Create the main window
root = tk.Tk()
root.title("Password Generator")
# Variables for user inputs
length_var = tk.StringVar(value='12')
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
similar_var = tk.BooleanVar(value=False)
result_var = tk.StringVar()
# GUI Layout
tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky='w')
tk.Entry(root, textvariable=length_var).grid(row=0, column=1, columnspan=2, sticky='ew')
tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).grid(row=1, column=0, sticky='w')
tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var).grid(row=1, column=1, sticky='w')
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=1, column=2, sticky='w')
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=2, column=0, sticky='w')
tk.Checkbutton(root, text="Exclude Similar Characters", variable=similar_var).grid(row=2, column=1, sticky='w')
tk.Button(root, text="Generate Password", command=generate_password).grid(row=3, column=0, columnspan=3, sticky='ew')
tk.Label(root, text="Generated Password:").grid(row=4, column=0, sticky='w')
tk.Entry(root, textvariable=result_var, state='readonly').grid(row=4, column=1, columnspan=2, sticky='ew')
# Run the application
root.mainloop()
