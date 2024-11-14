task_list = []
task_completed_list = []

def display_menu():
    print("Hello, welcome to the task manager")
    print("- Please select one of the following options:")
    print("     1. Add tasks")
    print("     2. Remove tasks")
    print("     3. Task Completed")
    print("     4. View tasks to do")
    print("     5. View completed tasks")
    print("     6. Exit")

def add_task():
    task = input("Enter the task: ")
    task_list.append(task)
    print(f"{task} added successfully")
    return task_list

def remove_task():
    task = input("Enter the task to remove: ")
    if task in task_list:
        task_list.remove(task)
        print(f"{task} removed successfully")
    else:
        print("Task not found")
    return task_list

def task_completed():
    task = input("Enter the task completed: ")
    task_list.remove(task)
    task_completed_list.append(task)
    print(f"{task} completed successfully")
    return task_list, task_completed_list

def view_tasks():
    if len(task_list) == 0:
        print("Vide")
    for task in task_list:
        print(task)

def view_tasks_completed():
    if len(task_completed_list) == 0:
        print("Vide")
    else:
        for task in task_completed_list:
            print(task)

def main():
    display_menu()
    while True:
        option = input("Enter your option: ")
        if option == "1":
            add_task()
        elif option == "2":
            remove_task()
        elif option == "3":
            task_completed()
        elif option == "4":
            view_tasks()
        elif option == "5":
            view_tasks_completed()
        elif option == "6":
            break

main()