import tkinter as tk
from tkinter import simpledialog
tasks = []
def add_task():
    task = simpledialog.askstring("Input", "Enter a task:")
    if task:
        tasks.append({'task': task, 'completed': False})
        listbox.insert(tk.END, task)
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        listbox.delete(selected_task_index)
def complete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task = tasks[selected_task_index[0]]
        task['completed'] = True
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, f"{task['task']} (Done)")
root = tk.Tk()
root.title("To-Do List")
frame = tk.Frame(root)
frame.pack(pady=10)
listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, padx=10)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=5)
complete_button = tk.Button(button_frame, text="Complete Task", command=complete_task)
complete_button.grid(row=0, column=2, padx=5)
root.mainloop()
