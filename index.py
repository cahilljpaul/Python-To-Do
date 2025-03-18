# List to store tasks 
tasks = []

# Function to add tasks
def show_tasks():
    """Display the tasks"""
    if not tasks:
        print("No tasks")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
show_tasks()

#Add a new task 
def add_task():
    """Add a new task"""
    task = input("/ Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added")
add_task()
show_tasks()
