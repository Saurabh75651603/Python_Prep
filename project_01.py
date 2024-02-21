import pickle


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


def main():
    todo_list = ToDoList('tasks.pkl')

    while True:
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            task_id = len(todo_list.tasks) + 1
            task = Task(task_id, description)
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            task_id = int(input("Enter task ID to mark as completed: "))
            for task in todo_list.tasks:
                if task.task_id == task_id:
                    task.mark_completed()
                    print("Task marked as completed!")
                    break
            else:
                print("Task not found!")
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            for task in todo_list.tasks:
                if task.task_id == task_id:
                    todo_list.tasks.remove(task)
                    todo_list.save_tasks()
                    print("Task deleted successfully!")
                    break
            else:
                print("Task not found!")
        elif choice == '4':
            print("All Tasks:")
            for task in todo_list.tasks:
                print(f"Task ID: {task.task_id}, Description: {task.description}, Completed: {task.completed}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
