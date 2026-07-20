# Simple To-Do List App in Python

tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()

    choice = input("Enter your choice (1-4): ")


    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_num = int(input("Enter task number to remove: "))
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed!")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")