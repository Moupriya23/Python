# Initialize an empty list to store tasks
tasks = []
# Function to display the available options
def display_menu():
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Exit")
# Start an infinite loop to continuously interact with the user
while True:
# Display the menu options
    display_menu()
# Get the user's choice
    choice = input("Select an option: ")
#Option 1: Add Task
    if choice =='1':
# Prompt the user to entera task
        task = input("Enter task:")
#Add the task to the list
        tasks.append(task)
        print("Task added successfully.")
#Option 2: Edit Task
    elif choice == '2':
# Check if there are tasks available to edit
        if tasks:
# Display the current tasks with their indices
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")

# Prompt the user to enter the index of the task to edit
            try:
                task_index = int(input("Enter task index to edit: ")) -1
# Check if the entered index is valid
                if 0 <= task_index < len(tasks):
# Prompt the user to entera new task
                    new_task= input("Enter new task: ")
# Update the task at the specified index
                    tasks[task_index] = new_task
                    print("Task edited successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available to edit.")
#Option 3: Delete Task
    elif choice =='3':
# Check if there are tasks available to delete
        if tasks:
# Display the current tasks with their indices 
            for index, task in enumerate(tasks):
# Prompt the user to enter the index of the task to delete
                print(f"{index + 1}. {task}")
            try:
                task_index = int(input("Enter task index to delete: ")) -1
# Check if the entered index is valid
                if 0 <= task_index < len(tasks):
# Remove the task at the specified index
                    tasks.pop(task_index)
                    print("Task deleted successfully.")
                else:
                    print("Invalid index.")

            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available to delete.")
#Option 4: Exit
    elif choice =='4':
#Exit the application
        print("Exiting the application. Goodbye !")
        break
# Handle invalid menu choices
    else:
        print("Invalid choice. Please select a valid option.")