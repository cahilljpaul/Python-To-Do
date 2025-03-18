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
