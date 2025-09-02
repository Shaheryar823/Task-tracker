import json
import datetime
import os

FILENAME = "tasks.json"
Json_file = []
id = 100

#load task from file
def load_task():
    global Json_file, id
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            Json_file = json.load(f)
        if Json_file:
            id = Json_file[-1]["id"]
    else:
        Json_file = []

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(Json_file, f, indent=4)

def add(description, status):
    global id
    id += 1 
    task = {
        "id" : id,
        "description" : description,
        "status" : status,
        "createdAt" : datetime.datetime.now().isoformat()
    }
    Json_file.append(task)
    save_tasks()
    display(Json_file)
    return task

def update_task(propose):
    if not Json_file:
        print("No tasks found.")
    else:
        task_id = int(input("Enter the task id : "))
        found = False
        for i in Json_file:
            if i["id"] == task_id:
                if propose == "del":
                    Json_file.remove(i)
                    print(f"{i['id']} deleted")
                elif propose == "status":
                    i['status'] = get_valid_status()
                save_tasks()
                found = True
                break
        display(Json_file)
        if not found:
            print("task not found")

def show_menu():
    os.system('cls')
    print("-------Main Menu--------------")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Update the status")
    print("5. List tasks that are done")
    print("6. List tasks in progress")
    print("7. List tasks that are pending")

def filter_tasks_by_status(status):
    print(f"Status with status {status}")
    filtered = [task for task in Json_file if task['status'] == status]
    display(filtered)

def display(json_file):
    os.system("cls")
    if not json_file:
        print("No tasks to display.")
        return

    # Header
    print("-" * 80)
    print(f"{'ID':<5} {'Description':<30} {'Status':<12} {'Created At'}")
    print("-" * 80)

    # Rows
    for task in json_file:
        print(f"{task['id']:<5} {task['description']:<30} {task['status']:<12} {task['createdAt']}")
    print("-" * 80)


def get_valid_status():
    print("Choose task status:")
    print("1. Pending")
    print("2. In Progress")
    print("3. Done")
    
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        return "pending"
    elif choice == "2":
        return "progress"
    elif choice == "3":
        return "done"
    else:
        print("Invalid choice! Defaulting to 'pending'.")
        return "pending"



# --- Example usage ---
load_task()  # load existing tasks
start_program = True
while start_program == True:
    entry = input("Press S or s to see the menu and Q or q to quit the program. ")
    if entry == 'S' or entry == 's':
        os.system('cls')
        show_menu()
        no = int(input("entry your number : "))
        if no == 1:
            description = input("Enter your task : ")
            status = get_valid_status()
            add(description, status)
        elif no == 2:
            if not Json_file:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                display(Json_file)
        elif no == 3:
            update_task("del")
        elif no == 4:
            
            update_task("status")
        elif no == 5:
            filter_tasks_by_status('done')
        elif no == 6:
            filter_tasks_by_status('progress')
        elif no == 7:
            filter_tasks_by_status('pending')
        else:
            print("Not Found")

        start_program = True
    else:
        os.system("cls")
        start_program =False
    
