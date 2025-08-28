import os

# Custom folder for saving the to-do list file
SAVE_FOLDER = "Simple to do list/todo_files"
TASK_FILE = os.path.join(SAVE_FOLDER, "todo_tasks.txt")

# Make sure the directory exists
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Load tasks from the file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file if line.strip()]
    return tasks

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a task
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 Your to-do list is empty.")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Remove a task
def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Removed task: {removed}")
    else:
        print("❌ Invalid task number.")

# Main menu loop
def main():
    print("📋 Welcome to the Simple To-Do List App")
    while True:
        print("\nChoose an action:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            task = input("Enter the task: ").strip()
            if task:
                add_task(task)
            else:
                print("⚠️ Task cannot be empty.")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to remove: "))
                remove_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            print("👋 Exiting. Have a productive day!")
            break
        else:
            print("❗ Invalid choice. Please select from 1 to 4.")

# Run the program
main()
