alltask = []

def addtask():
    name = input("Enter Task Name: ")
    alltask.append(name)
    print("Task Added")
    print(alltask)
    return name

def removetask():
    print(alltask)
    if len(alltask) == 0:
        print("No tasks to remove.")
        return
    choose = int(input(f"Enter the task number b/w (0 to {len(alltask) - 1}): "))
    if choose < 0 or choose >= len(alltask):
        print("Invalid choice.")
    else:
        del alltask[choose]
        print("Task remove successfully ")
    print(alltask)

def updatetask():
    
    if len(alltask) == 0:
        print("Your Task List is empty")
        return
    print(alltask)
    choose = int(input(f"Enter the task number to update b/w (0 to {len(alltask) - 1}): "))
    if choose < 0 or choose >= len(alltask):
        print("Invalid choice!")
    else:
        new_task = input("Enter Your new task: ")
        alltask[choose] = new_task
        print("Task updated!")
        print(alltask)

def sorting():
    if len(alltask) == 0:
        print("No tasks to sort.")
        return
    print("Current Task List:")
    print(alltask)
    order = int(input("Sort Order\n 1. accending \n 2. decending\n "))
    if order == 1:
        alltask.sort()
        print("Tasks sorted in ascending order.")
    elif order == 2:
        alltask.sort(reverse=True)
        print(f"Tasks sorted in descending order.\n{alltask}")
    else:
        print("Wrong Input")
    print(alltask)

while True:
    print(">>> Task Manager <<<".upper())
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. Sort Tasks")
    print("5. Exit")

    option = int(input("Enter your choice: "))
    if option == 1:
        print("Adding")
        addtask()
    elif option == 2:
        print("Removing")
        removetask()
    elif option == 3:
        print("Updating")
        updatetask()
    elif option == 4:
        print("Sorting")
        sorting()
    elif option == 5:
        print("Stopping")
        break
    else:
        print("Incorrect!! Please enter number b/w 1 to 5 only")
