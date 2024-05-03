import tkinter as tk
from datetime import datetime
from tkcalendar import DateEntry
from todo import Task
from tkinter import ttk

class AddTaskWindow:
    def __init__(self, master, database, tasks, callback):
        self.master = master
        self.database = database
        self.tasks = tasks
        self.callback = callback

        self.top = tk.Toplevel(master)
        self.top.title("Add Task")

        tk.Label(self.top, text="Title:").pack()
        self.title_entry = tk.Entry(self.top)
        self.title_entry.pack()

        tk.Label(self.top, text="Description:").pack()
        self.description_entry = tk.Entry(self.top)
        self.description_entry.pack()

        # Calendar Picker for Date
        tk.Label(self.top, text="Date:").pack()
        self.date_entry = DateEntry(self.top, date_pattern="yyyy-mm-dd")
        self.date_entry.pack()

        # Time Picker
        tk.Label(self.top, text="Time:").pack()
        self.time_picker = ttk.Combobox(self.top, values=self.get_time_options())
        self.time_picker.pack()

        add_button = tk.Button(self.top, text="Add Task", command=self.add_task)
        add_button.pack(pady=10)

    def get_time_options(self):
        # Generate time options from 00:00 to 23:45 with 15-minute intervals
        times = []
        for hour in range(0, 24):
            for minute in range(0, 60, 60):
                time_str = f"{hour:02d}:{minute:02d}"
                times.append(time_str)
        return times

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        date = self.date_entry.get()
        time = self.time_picker.get()

        if title and date and time:
            new_task = Task(task_id=None, title=title, description=description, status="Pending", date=date, time=time)
            task_id = self.database.create_task(new_task)
            new_task.task_id = task_id
            self.tasks.append(new_task)
            self.callback()
            self.top.destroy()