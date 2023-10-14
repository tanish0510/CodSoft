import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle

tasks = {}

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert('', 'end', values=(task,))
        tasks[task] = False
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = task_listbox.selection()
    if selected_task_index:
        selected_task = task_listbox.item(selected_task_index, "values")[0]
        del tasks[selected_task]
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def mark_completed():
    selected_task_index = task_listbox.selection()
    if selected_task_index:
        selected_task = task_listbox.item(selected_task_index, "values")[0]
        tasks[selected_task] = True
        task_listbox.delete(selected_task_index)
        completed_listbox.insert('', 'end', values=(selected_task,))
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def mark_uncompleted():
    selected_task_index = completed_listbox.selection()
    if selected_task_index:
        selected_task = completed_listbox.item(selected_task_index, "values")[0]
        tasks[selected_task] = False
        completed_listbox.delete(selected_task_index)
        task_listbox.insert('', 'end', values=(selected_task,))
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as uncompleted.")

root = tk.Tk()
root.title(" To-Do List ")
root.geometry("600x400")

style = ThemedStyle(root)
style.set_theme("radiance")

notebook = ttk.Notebook(root)
notebook.pack(pady=20, padx=20, fill="both", expand=True)

todo_tab = ttk.Frame(notebook)
notebook.add(todo_tab, text="To-Do")

frame = ttk.Frame(todo_tab)
frame.pack(pady=20)

task_entry = ttk.Entry(frame, font=("Arial", 14), style="TEntry")
task_entry.grid(row=0, column=0, padx=5)

add_button = ttk.Button(frame, text="Add Task", command=add_task, style="TButton")
add_button.grid(row=0, column=1, padx=5)

remove_button = ttk.Button(frame, text="Remove Task", command=remove_task, style="TButton")
remove_button.grid(row=0, column=2, padx=5)

mark_button = ttk.Button(frame, text="Mark Completed", command=mark_completed, style="TButton")
mark_button.grid(row=0, column=3, padx=5)

task_listbox = ttk.Treeview(todo_tab, columns=("Task",), show="headings")
task_listbox.heading("Task", text="Task")
task_listbox.pack(pady=10, padx=20, fill="both", expand=True)

completed_tab = ttk.Frame(notebook)
notebook.add(completed_tab, text="Completed")

completed_listbox = ttk.Treeview(completed_tab, columns=("Task",), show="headings")
completed_listbox.heading("Task", text="Task")
completed_listbox.pack(pady=10, padx=20, fill="both", expand=True)

mark_uncompleted_button = ttk.Button(completed_tab, text="Mark Uncompleted", command=mark_uncompleted, style="TButton")
mark_uncompleted_button.pack()

root.mainloop()
