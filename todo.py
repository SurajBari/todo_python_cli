class TodoApp:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the list.')

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f'Task "{removed_task}" removed from the list.')
        else:
            print("Invalid task number.")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. View tasks")
            print("2. Add task")
            print("3. Delete task")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '3':
                self.display_tasks()
                try:
                    task_index = int(input("Enter the task number to delete: ")) - 1
                    self.delete_task(task_index)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                print("Exiting the To-Do app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_app = TodoApp()
    todo_app.run()
