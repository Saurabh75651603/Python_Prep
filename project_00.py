import pickle
import tkinter as tk
from tkinter import messagebox


class Task:
    def __init__(self, task_id, description, completed=False):
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True


class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.tasks, f)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    # Implement other methods like mark_task_complete, delete_task, etc.


class TodoListApp:
    def __init__(self, root, todo_list):
        self.root = root
        self.root.title("To-Do List")
        self.todo_list = todo_list

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack(padx=10, pady=10)

        self.refresh_tasks()

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        mark_complete_button = tk.Button(root, text="Mark Task as Completed", command=self.mark_completed)
        mark_complete_button.pack(pady=5)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)

        exit_button = tk.Button(root, text="Exit", command=root.quit)
        exit_button.pack(pady=5)

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, f"Task ID: {task.task_id}, Description: {task.description}, Completed: {task.completed}")

    def add_task(self):
        description = tk.simpledialog.askstring("Add Task", "Enter task description:")
        task_id = len(self.todo_list.tasks) + 1
        task = Task(task_id, description)
        self.todo_list.add_task(task)
        self.refresh_tasks()

    def mark_completed(self):
        task_index = self.task_listbox.curselection()
        if task_index:
            task_id = int(task_index[0]) + 1
            for task in self.todo_list.tasks:
                if task.task_id == task_id:
                    task.mark_completed()
                    self.todo_list.save_tasks()
                    self.refresh_tasks()
                    messagebox.showinfo("Task Completed", "Task marked as completed!")
                    break
            else:
                messagebox.showerror("Error", "Task not found!")
        else:
            messagebox.showerror("Error", "Please select a task to mark as completed.")

    def delete_task(self):
        task_index = self.task_listbox.curselection()
        if task_index:
            task_id = int(task_index[0]) + 1
            for task in self.todo_list.tasks:
                if task.task_id == task_id:
                    self.todo_list.tasks.remove(task)
                    self.todo_list.save_tasks()
                    self.refresh_tasks()
                    messagebox.showinfo("Task Deleted", "Task deleted successfully!")
                    break
            else:
                messagebox.showerror("Error", "Task not found!")
        else:
            messagebox.showerror("Error", "Please select a task to delete.")


def main():
    todo_list = ToDoList('tasks.pkl')

    root = tk.Tk()
    app = TodoListApp(root, todo_list)
    root.mainloop()


if __name__ == "__main__":
    main()
