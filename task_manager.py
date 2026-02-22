task_list=[]

while True:
    print("1.Add a task")
    print("2.view all task")
    print("3.Update status")
    print("4.Delete task")
    print("5.exit")

    choice = int(input("What do you want to do? "))

    #add task
    if choice == 1:
        task_name = input("Enter task name: ")
        priority = input("Priority (high/Medium/Low): ")
        status = input("Enter task status (Pending/Done)")

        task_dict = {
            "task": task_name ,
            "priority": priority,
            "status": status
            }
        
        task_list.append(task_dict)
        print("task added successfully")

    
    #view task
    elif choice == 2:
        if not task_list:
            print("NO task available")

        else:
            priority_order ={"High":1, "Medium":2, "Low":3}
            sorted_task = sorted(task_list,key=lambda x: priority_order[x["priority"]])

            for i, task in enumerate(sorted_task):
                print(f"{i}. {task}")


        # UPDATE STATUS
    elif choice == 3:
        index = int(input("Enter task number to update: "))
        if 0 <= index < len(task_list):
            new_status = input("Enter new status (Pending / Done): ")
            task_list[index]["status"] = new_status
            print("Status updated!")
        else:
            print("Invalid task number.")

    # DELETE TASK
    elif choice == 4:
        index = int(input("Enter task number to delete: "))
        if 0 <= index < len(task_list):
            task_list.pop(index)
            print("Task deleted!")
        else:
            print("Invalid task number.")

    # EXIT
    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("invalid choice.")
