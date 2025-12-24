print("<=====My To Do List=====>")

to_do_list = []
 # Start with empty list
# This list will store all our tasks as strings
# Example after adding tasks: ["Buy milk", "Walk dog", "Study Python"]
while True:
    # while True = loop forever (until we use 'break')
    # This creates a "menu loop" pattern
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Edit task")
    print("4. Complete task")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")
    if choice == "1":
        task = input("Enter the task to add: ")
        to_do_list.append(task)
        #  append() adds the task to the END of the list
    # Before: todos = ["Walk dog"]
    # After:  todos = ["Walk dog", "Buy groceries"]
        print(f'Task "{task}" added to your to-do list.')
    elif choice == "2":
        if len(to_do_list) == 0:
            # len(todos) = number of items in list
        # If 0, list is empty
            print("Your to-do list is empty. Nothing to edit.")
        else:
            print("Your to-do list:")   
            for index, task in enumerate(to_do_list):
                # enumerate() gives us index AND item
            # Example: todos = ["Buy milk", "Walk dog"]
            # Loop 1: i=0, task="Buy milk"
            # Loop 2: i=1, task="Walk dog"
                print(f"{index + 1}. {task}")
                            # i + 1 because we want to show 1, 2, 3... not 0, 1, 2...
    elif choice == "3":
        if len(to_do_list) == 0:
            print("Your to-do list is empty. Nothing to edit.")
        else:
            print("Your to-do list:")
            for index, task in enumerate(to_do_list):
                print(f"{index + 1}. {task}")
            task_num = int(input("Enter the task number to edit: "))
            if 1 <= task_num <= len(to_do_list):
                # Check if index is valid
            # 1 <= index means: index is 1 or higher
            # index < len(todos) means: index isn't too big
                new_task = input("Enter the new task description: ")
                to_do_list[task_num - 1] = new_task
                print(f'Task {task_num} updated to "{new_task}".')
            else:
                print("Invalid task number.")
    elif choice == "4":
        if len(to_do_list) == 0:
            print("Your to-do list is empty. Nothing to complete.")
        else:
            print("Your to-do list to complete:")
            for index, task in enumerate(to_do_list):
                print(f"{index + 1}. {task}")
            task_num = int(input("Enter the task number to complete: "))
            if 1 <= task_num <= len(to_do_list):
                completed_task = to_do_list.pop(task_num - 1)
                 # pop(index) removes item at that position AND returns it
            # Before: todos = ["Buy milk", "Walk dog", "Study"]
            # todos.pop(1) removes "Walk dog" and returns it
            # After:  todos = ["Buy milk", "Study"]
                print(f'Task "{completed_task}" completed and removed from your to-do list.')
            else:
                print("Invalid task number.")
    elif choice == "5":
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1-5).")


                
                 
