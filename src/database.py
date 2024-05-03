import mysql.connector
from todo import Task

class Database:
    def __init__(self, host, username, password, database):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="todo_db"
        )
        self.cursor = self.connection.cursor()

    def create_task(self, task):
        sql = "INSERT INTO tasks (title, description, status, date, time) VALUES (%s, %s, %s, %s, %s)"
        values = (task.title, task.description, task.status, task.date, task.time)
        self.cursor.execute(sql, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def update_task(self, task):
        sql = "UPDATE tasks SET title=%s, description=%s, status=%s, date=%s, time=%s WHERE id=%s"
        values = (task.title, task.description, task.status, task.date, task.time, task.task_id)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def delete_task(self, task_id):
        sql = "DELETE FROM tasks WHERE id=%s"
        self.cursor.execute(sql, (task_id,))
        self.connection.commit()

    def get_tasks(self):
        sql = "SELECT * FROM tasks"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        tasks = []
        for row in rows:
            task = Task(row[0], row[1], row[2], row[3], row[4], row[5])
            tasks.append(task)
        return tasks