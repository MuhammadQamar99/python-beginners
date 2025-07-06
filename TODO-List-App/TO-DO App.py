# Day 10 - To-Do List App by Muhammad Qamar

todo_list = []

def show_menu():
    print("\n======== To-Do List Menu ========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("=================================")

def View_Task():
    if not todo_list:
        print("NO TASK FOUND")
    else:
        print("\n==== Your Task ====")
        for idx, task in enumerate(todo_list, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{idx}. {task} ({status})")

def add_task():
    task = input("Enter new task: ")
    todo_list.append({'task': task, 'done': False})
    print("Task added successfully!")

def mark_done():
    if not todo_list:
        print("NO TASK FOUND")
    else:
        View_Task()
        task_no = int(input("Enter task number to mark as done: "))
        if task_no > 0 and task_no <= len(todo_list):
            todo_list[task_no - 1]['done'] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")

def delete_task():
    if not todo_list:
        print("NO TASK FOUND")
    else:
        View_Task()
        task_no = int(input("Enter Task number to remove task: "))
        if task_no > 0 and task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Task '{removed['task']}' removed.")
        else:
            print("Invalid task number.")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        View_Task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")