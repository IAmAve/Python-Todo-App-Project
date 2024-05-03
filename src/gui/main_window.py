import tkinter as tk
from gui.add_task_window import AddTaskWindow
from gui.edit_task_window import EditTaskWindow
from database import Database
from todo import Task

class MainWindow:
    def __init__(self, master):
        self.master = master

        self.database = Database(host='localhost', username='your_username', password='your_password', database='todo_app')

        self.tasks = self.database.get_tasks()

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.pack(padx=10, pady=10)

        self.populate_tasks()

        add_button = tk.Button(master, text="Add Task", command=self.open_add_task_window)
        add_button.pack(padx=10, pady=5)

        edit_button = tk.Button(master, text="Edit Task", command=self.open_edit_task_window)
        edit_button.pack(padx=10, pady=5)

        delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        delete_button.pack(padx=10, pady=5)

    def populate_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task.title} - {task.date} {task.time}")

    def open_add_task_window(self):
        AddTaskWindow(self.master, self.database, self.tasks, self.populate_tasks)

    def open_edit_task_window(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]
            EditTaskWindow(self.master, selected_task, self.database, self.populate_tasks)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.tasks[selected_index[0]]
            self.database.delete_task(selected_task.task_id)
            self.tasks.remove(selected_task)
            self.populate_tasks()