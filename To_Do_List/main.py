#This is a To-Do List app

tasks: list[str] = []

def menu():
    print(f"\nPress 1 to Add Task")
    print(f"Press 2 to Edit Task")
    print(f"Press 3 to Delete Task")
    print(f"Press 4 to View All Tasks")
    print(f"Press 5 to Exit")
    task=input(f"Enter the command\n: ")

    return task

def add_task():
    input_task=input(f"Enter the task\n: ")
    tasks.append(input_task)

def edit_task():
    editTask=int(input("which task to edit\n<0,1,2,3,4,....>\n: "))
    new_task: str = input(f"Enter the new task\n: ")
    if editTask=="":
        print(f" Original Task is ['{tasks[len(tasks)]}'] Edited Task is ['{new_task}'] ")
        tasks[len(tasks)] = new_task
    else:
         print(f" Original Task is ['{tasks[editTask]}'] Edited Task is ['{new_task}'] ")
         tasks[editTask] = new_task

def delete_task():
    deleteTask = int(input("which task to delete\n<0,1,2,3,4,....>\n: "))
    if deleteTask=="":
        return tasks.pop()
    else:
        deleted_task = tasks.pop(deleteTask)
        return deleted_task

def view_all_tasks():
    print(f"S.No \t Tasks")
    for i in range(len(tasks)):
        task=tasks[i]
        print(f"{i} :  {task}")

def main():
    commands_only=["1","2","3","4"]
    while True:
        task=menu()
        if task in commands_only:
            if task=="1":
                add_task()
            elif task=="2":
                edit_task()
            elif task=="3":
                print(f"Deleted Tasks\n: '{delete_task()}'")
            elif task=="4":
                view_all_tasks()
            elif task=="5":
                print("Exiting...")
                break
        elif task=="5":
            print("Exiting...")
            break
        else:
            print(f"Invalid command. Please try again.")


if __name__=="__main__":
    main()