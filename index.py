# List to store tasks 
tasks = []

# Function to show tasks
def show_tasks():
    """Display the tasks"""
    if not tasks:
        print("No tasks")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a new task 
def add_task():
    """Add a new task"""
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added")

# Main loop
def main():
    while True:
        print("\nChoose an option:")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()