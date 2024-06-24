import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

# Function to add a task
def add_task():
    task = task_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    
    if task and date and time:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
            task_with_time = f"{task} (Due: {date} at {time})"
            tasks_listbox.insert(tk.END, task_with_time)
            task_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            time_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning("Warning", "Invalid date or time format! Use YYYY-MM-DD for date and HH:MM for time.")
    else:
        messagebox.showwarning("Warning", "Task, date, and time cannot be empty!")

# Function to update a selected task
def update_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        current_task = tasks_listbox.get(selected_task_index)
        new_task = simpledialog.askstring("Input", "Enter new task:", initialvalue=current_task.split(" (Due:")[0])
        new_date = simpledialog.askstring("Input", "Enter new date (YYYY-MM-DD):", initialvalue=current_task.split("Due: ")[1].split(" at ")[0])
        new_time = simpledialog.askstring("Input", "Enter new time (HH:MM):", initialvalue=current_task.split(" at ")[1][:-1])
        
        if new_task and new_date and new_time:
            try:
                datetime.strptime(new_date, "%Y-%m-%d")
                datetime.strptime(new_time, "%H:%M")
                task_with_time = f"{new_task} (Due: {new_date} at {new_time})"
                tasks_listbox.delete(selected_task_index)
                tasks_listbox.insert(selected_task_index, task_with_time)
            except ValueError:
                messagebox.showwarning("Warning", "Invalid date or time format! Use YYYY-MM-DD for date and HH:MM for time.")
        else:
            messagebox.showwarning("Warning", "Task, date, and time cannot be empty!")
    else:
        messagebox.showwarning("Warning", "No task selected!")

# Function to delete a selected task
def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "No task selected!")

# Setting up the GUI
root = tk.Tk()
root.title("To-Do List")

# Styles
bg_color = "#f0f0f0"
button_color = "#4CAF50"
button_fg = "white"
font = ("Helvetica", 12)

root.config(bg=bg_color)

# Input fields for task
tk.Label(root, text="Task:", bg=bg_color, font=font).grid(row=0, column=0, padx=10, pady=10, sticky="e")
task_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
task_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Due Date (YYYY-MM-DD):", bg=bg_color, font=font).grid(row=1, column=0, padx=10, pady=10, sticky="e")
date_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
date_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Due Time (HH:MM):", bg=bg_color, font=font).grid(row=2, column=0, padx=10, pady=10, sticky="e")
time_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
time_entry.grid(row=2, column=1, padx=10, pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task, bg=button_color, fg=button_fg, font=font)
add_button.grid(row=0, column=2, padx=10, pady=10)

update_button = tk.Button(root, text="Update Task", command=update_task, bg="#2196F3", fg="white", font=font)
update_button.grid(row=1, column=2, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=font)
delete_button.grid(row=2, column=2, padx=10, pady=10)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=15, font=("Helvetica", 14))
tasks_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Run the application
root.mainloop()
