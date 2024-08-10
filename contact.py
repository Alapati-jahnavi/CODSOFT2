import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")
contacts = []
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone:
        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Error", "Name and Phone number are required.")
def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")
def search_contact():
    search_term = search_entry.get()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")
def update_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        contacts[index] = {'name': name_entry.get(), 'phone': phone_entry.get(), 'email': email_entry.get(), 'address': address_entry.get()}
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Error", "No contact selected.")
def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        del contacts[index]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        view_contacts()
    else:
        messagebox.showwarning("Error", "No contact selected.")
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
tk.Label(root, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
tk.Label(root, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)
tk.Label(root, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)
tk.Label(root, text="Address").grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)
tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=6, column=0, columnspan=2)
tk.Label(root, text="Search").grid(row=7, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=7, column=1)
tk.Button(root, text="Search", command=search_contact).grid(row=7, column=2)
contact_list = tk.Listbox(root)
contact_list.grid(row=8, column=0, columnspan=3)
root.mainloop()
