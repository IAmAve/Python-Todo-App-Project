import tkinter as tk
from datetime import datetime
from todo import Task

class EditTaskWindow:
    def __init__(self, master, task, database, callback):
        self.master = master
        self.task = task
        self.database = database
        self.callback = callback

        self.top = tk.Toplevel(master)
        self.top.title("Edit Task")

        tk.Label(self.top, text="Title:").pack()
        self.title_entry = tk.Entry(self.top)
        self.title_entry.insert(tk.END, task.title)
        self.title_entry.pack()

        tk.Label(self.top, text="Description:").pack()
        self.description_entry = tk.Entry(self.top)
        self.description_entry.insert(tk.END, task.description)
        self.description_entry.pack()

        tk.Label(self.top, text="Date (YYYY-MM-DD):").pack()
        self.date_entry = tk.Entry(self.top)
        self.date_entry.insert(tk.END, task.date)
        self.date_entry.pack()

        tk.Label(self.top, text="Time (HH:MM):").pack()
        self.time_entry = tk.Entry(self.top)
        self.time_entry.insert(tk.END, task.time)
        self.time_entry.pack()

        edit_button = tk.Button(self.top, text="Save Changes", command=self.edit_task)
        edit_button.pack(pady=10)

    def edit_task(self):
        new_title = self.title_entry.get()
        new_description = self.description_entry.get()
        new_date = self.date_entry.get()
        new_time = self.time_entry.get()

        if new_title and new_date and new_time:
            self.task.title = new_title
            self.task.description = new_description
            self.task.date = new_date
            self.task.time = new_time
            self.database.update_task(self.task)
            self.callback()
            self.top.destroy()