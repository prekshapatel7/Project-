import json
import os

# Load existing tasks if file exists
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Display menu
def show_menu():
    print("\n📝 To-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

# Main app loop
tasks = load_tasks()

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("\n📋 Tasks:")
        for i, task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{i+1}. {task['task']} {status}")

    elif choice == '2':
        new_task = input("Enter task: ")
        tasks.append({"task": new_task, "done": False})
        print("Task added!")

    elif choice == '3':
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done!")

    elif choice == '4':
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"Deleted: {deleted['task']}")

    elif choice == '5':
        save_tasks(tasks)
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
