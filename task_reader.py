from pathlib import Path

# =======================================
# Module responsible for reading and selecting 
# tasks from the 'tasks' directory.
# =======================================

def get_task_name():
    # Specify the directory path
    folder_path = Path("./tasks")

    # List only files (excluding subfolders)
    file_names = sorted(
        file.stem
        for file in folder_path.iterdir()
        if file.is_file() and file.suffix == ".md"
    )
    checked = False

    while checked == False:

        # Print the available tasks
        print("="*15+" Available Tasks "+"="*15)
        print('')

        for i, name in enumerate(file_names):
            print(f"{i}: {name}")
        
        print('')
        print("="*50)

        task_index = input("Type the index of the task you want to generate (or type 'quit' to exit): ")
        print('')
        # Check if the user wants to quit
        if task_index.lower() == "quit":
            return None

        # Validate the input and get the task name
        try:
            task_name = file_names[int(task_index)]
            print(f"Task '{task_name}' found.")
            print('')
            checked = True  

        # Handle invalid input
        except (ValueError, IndexError):
            print(f"Invalid index. Please try again.")
            print('')
            checked = False

    return task_name