##to-do list

task_list=[]

def main_menu():
    print("MENU LIST")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")

while True:
    main_menu()
    choice= input("Choose an option(1-5): ")

    if choice=='1':
        task= input("Enter your task: ")
        task_list.append({"task":task})
        print("Task added!")

    elif choice=='2':
        print("##Your tasks:")
        if not task:
            print("No tasks yet")
        else:
            for task in task_list:
                print(task)
    
    elif choice=='3':
        if not task_list:
            print("No tasks to be marked")
        else:
            task_num= int(input("Enter the task number you want marked as done: "))-1
            if 0<=task_num<len(task_list):
                task_list[task_num]["status"]= True
                print("task marked as complete!")
            else:
                print("Invalid task")
    
    elif choice=='4':
        if not task_list:
            print("No tasks to be deleted")
        else:
            task_num= int(input("Enter the task number you want to delete: "))-1
            if 0<=task_num<len(task_list):
                deleted= task_list.pop(task_num)
                print("Task deleted was: ", deleted)
            else:
                print("Invalid task")
    
    elif choice=='5':
        print("Goodbye!")
        break

    else:
        print("Invalid option!!")



